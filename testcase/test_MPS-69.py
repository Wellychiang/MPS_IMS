from . import pytest
from . import allure
from . import teamlist
from . import player
from . import log
from . import base
from . import re
import time


@allure.feature('Team list in agent team')
@allure.story('Verify different level and status with search.')
@allure.step('')
def test_search_function(username='ssh001',
                         updater='crystal',
                         offsets=(0, 100, 200),
                         user_id='add111',
                         ):
    verify_ags_username_search(username=username)
    verify_ags_updater_search(updater=updater)
    verify_ags_all_levels_search(offsets=offsets)

    for level in range(1, 7):
        verify_ags_single_level_search(level)

    verify_ags_status_change_and_search(username=user_id)


def verify_ags_username_search(username):
    _, response = teamlist.ag_team_list_search(searchValue=username)
    lists_data = response['data']
    for list_data in lists_data:
        assert username in list_data['account']


def verify_ags_updater_search(updater):
    _, response = teamlist.ag_team_list_search(searchValue=updater, searchField='UPDATER')
    lists_data = response['data']
    for list_data in lists_data:
        assert updater == list_data['updater']


def verify_ags_all_levels_search(offsets):
    all_level_dict = {}
    for level in range(1, 7):
        all_level_dict.setdefault(level, 0)

    for page in offsets:
        _, response = teamlist.ag_team_list_search(searchValue=None,
                                            limit=100,
                                            offset=page)
        lists_data = response['data']
        for list_data in lists_data:
            all_level_dict[list_data['level']] += 1

    for k, v in all_level_dict.items():
        if v == 0:
            raise ValueError(f'Can not search all levels, all level items: {all_level_dict}')
        else:
            pass
    log(f'All level items: {all_level_dict}')


def verify_ags_single_level_search(levell):
    _, response = teamlist.ag_team_list_search(searchValue=None,
                                        limit=100,
                                        level=levell)
    log(f'Search level: {levell}')
    lists_data = response['data']
    for list_data in lists_data:
        pytest.assume(list_data['level'] == levell)
        if list_data['level'] == levell:
            continue
        else:
            raise ValueError(f'Search value is not equal search result, search level: {levell}')


def verify_ags_status_change_and_search(username):
    global user_id
    _, list_data = teamlist.ag_team_list_search(searchValue=username)

    lists_data = list_data['data']
    for list_data in lists_data:
        if 'add111' in list_data['account']:
            user_id = list_data['id']
        else:
            raise ValueError('Search failed')
    for status in range(1, 4):
        teamlist.agent_status_update(ag_id=user_id, value=status)
        _, response = teamlist.ag_team_list_search(searchValue=username, status=status)
        lists_data = response['data']
        if len(lists_data) == 0:
            raise ValueError(f'0 data in the this search, user: {username}, status: {status} ')
        for list_data in lists_data:
            if list_data['status'] != status:
                raise ValueError(f"Update status not equal ag report's status")
