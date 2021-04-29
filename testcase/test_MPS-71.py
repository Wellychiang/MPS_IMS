from . import pytest
from . import allure
from . import teamlist
from . import player
from . import log
from . import base
from . import re
import time


@allure.feature('Team list in agent team')
@allure.story('Scenario with verify split page.')
@allure.step('')
def test_split_page(username='wellyadmin',
                    ):
    _, page_one = teamlist.ag_team_list(username,
                                              status='0',
                                              level='0',
                                              searchValue=None,
                                              searchField='AGENT',
                                              sortColumn='ACCOUNT',
                                              sort='ASC',
                                              limit='25',
                                              offset='0',)
    _, page_two = teamlist.ag_team_list(username,
                                             status='0',
                                             level='0',
                                             searchValue=None,
                                             searchField='AGENT',
                                             sortColumn='ACCOUNT',
                                             sort='ASC',
                                             limit='25',
                                             offset='25',)
    _, team_list50 = teamlist.ag_team_list(username,
                                           status='0',
                                           level='0',
                                           searchValue=None,
                                           searchField='AGENT',
                                           sortColumn='ACCOUNT',
                                           sort='ASC',
                                           limit='50',
                                           offset='0',)
    _, team_list100 = teamlist.ag_team_list(username,
                                               status='0',
                                               level='0',
                                               searchValue=None,
                                               searchField='AGENT',
                                               sortColumn='ACCOUNT',
                                               sort='ASC',
                                               limit='100',
                                               offset='0',)
    pytest.assume(page_one != page_two)
    pytest.assume(len(team_list50['data']) == 50)
    assert len(team_list100['data']) == 100
