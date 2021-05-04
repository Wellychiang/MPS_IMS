from . import pytest
from . import allure
from . import teamlist
from . import player
from . import log
from . import base
from . import re
import time
import random
import os


@allure.feature('Team list in agent team')
@allure.story("Scenario for include agent and member then verify in team list")
@allure.step('')
def test_shinjen_button(ssh="ssh",
                        sh='sh',
                        ssma='ssma',
                        sma='sma',
                        ma='ma',
                        ag='ag',
                        ):
    os.system('del -r player.txt')
    os.system('del -r agent.txt')

    ssh_user, ssh_id = add_agent_and_return_agent_info(level_name=ssh, parentAccount=None, parentId=0, level=1)
    add_member(parentAccount=ssh_user, parentId=ssh_id)
    _, ssh_report = teamlist.ag_team_list_search(searchValue=ssh_user)
    verify_ag_team_list_search(ssh_report,
                                id=ssh_id,
                                account=ssh_user,
                                directDownLineCount=0,
                                downLinePlayerCount=1,
                                parentId=0)

    sh_user, sh_id = add_agent_and_return_agent_info(level_name=sh, parentAccount=ssh_user, parentId=ssh_id, level=2)
    add_member(parentAccount=sh_user, parentId=sh_id)
    _, ssh_report = teamlist.ag_team_list_search(searchValue=ssh_user)
    _, sh_report = teamlist.ag_team_list_search(searchValue=sh_user)
    verify_ag_team_list_search(ssh_report,
                                id=ssh_id,
                                account=ssh_user,
                                directDownLineCount=1,
                                downLinePlayerCount=2,
                                parentId=0)
    verify_ag_team_list_search(sh_report,
                                id=sh_id,
                                account=sh_user,
                                directDownLineCount=0,
                                downLinePlayerCount=1,
                                parentId=ssh_id)

    ssma_user, ssma_id = add_agent_and_return_agent_info(level_name=ssma, parentAccount=sh_user, parentId=sh_id, level=3)
    add_member(parentAccount=ssma_user, parentId=ssma_id)
    _, ssh_report = teamlist.ag_team_list_search(searchValue=ssh_user)
    _, sh_report = teamlist.ag_team_list_search(searchValue=sh_user)
    _, ssma_report = teamlist.ag_team_list_search(searchValue=ssma_user)
    verify_ag_team_list_search(ssh_report,
                                id=ssh_id,
                                account=ssh_user,
                                directDownLineCount=1,
                                downLinePlayerCount=3,
                                parentId=0)
    verify_ag_team_list_search(sh_report,
                                id=sh_id,
                                account=sh_user,
                                directDownLineCount=1,
                                downLinePlayerCount=2,
                                parentId=ssh_id)
    verify_ag_team_list_search(ssma_report,
                                id=ssma_id,
                                account=ssma_user,
                                directDownLineCount=0,
                                downLinePlayerCount=1,
                                parentId=sh_id)

    sma_user, sma_id = add_agent_and_return_agent_info(level_name=sma, parentAccount=ssma_user, parentId=ssma_id, level=4)
    add_member(parentAccount=sma_user, parentId=sma_id)
    _, ssh_report = teamlist.ag_team_list_search(searchValue=ssh_user)
    _, sh_report = teamlist.ag_team_list_search(searchValue=sh_user)
    _, ssma_report = teamlist.ag_team_list_search(searchValue=ssma_user)
    _, sma_report = teamlist.ag_team_list_search(searchValue=sma_user)
    verify_ag_team_list_search(ssh_report,
                                id=ssh_id,
                                account=ssh_user,
                                directDownLineCount=1,
                                downLinePlayerCount=4,
                                parentId=0)
    verify_ag_team_list_search(sh_report,
                                id=sh_id,
                                account=sh_user,
                                directDownLineCount=1,
                                downLinePlayerCount=3,
                                parentId=ssh_id)
    verify_ag_team_list_search(ssma_report,
                                id=ssma_id,
                                account=ssma_user,
                                directDownLineCount=1,
                                downLinePlayerCount=2,
                                parentId=sh_id)
    verify_ag_team_list_search(sma_report,
                                id=sma_id,
                                account=sma_user,
                                directDownLineCount=0,
                                downLinePlayerCount=1,
                                parentId=ssma_id)
    ma_user, ma_id = add_agent_and_return_agent_info(level_name=ma, parentAccount=sma_user, parentId=sma_id, level=5)
    add_member(parentAccount=ma_user, parentId=ma_id)
    _, ssh_report = teamlist.ag_team_list_search(searchValue=ssh_user)
    _, sh_report = teamlist.ag_team_list_search(searchValue=sh_user)
    _, ssma_report = teamlist.ag_team_list_search(searchValue=ssma_user)
    _, sma_report = teamlist.ag_team_list_search(searchValue=sma_user)
    _, ma_report = teamlist.ag_team_list_search(searchValue=ma_user)
    verify_ag_team_list_search(ssh_report,
                                id=ssh_id,
                                account=ssh_user,
                                directDownLineCount=1,
                                downLinePlayerCount=5,
                                parentId=0)
    verify_ag_team_list_search(sh_report,
                                id=sh_id,
                                account=sh_user,
                                directDownLineCount=1,
                                downLinePlayerCount=4,
                                parentId=ssh_id)
    verify_ag_team_list_search(ssma_report,
                                id=ssma_id,
                                account=ssma_user,
                                directDownLineCount=1,
                                downLinePlayerCount=3,
                                parentId=sh_id)
    verify_ag_team_list_search(sma_report,
                                id=sma_id,
                                account=sma_user,
                                directDownLineCount=1,
                                downLinePlayerCount=2,
                                parentId=ssma_id)
    verify_ag_team_list_search(ma_report,
                                id=ma_id,
                                account=ma_user,
                                directDownLineCount=0,
                                downLinePlayerCount=1,
                                parentId=sma_id)

    ag_user, ag_id = add_agent_and_return_agent_info(level_name=ag, parentAccount=ma_user, parentId=ma_id, level=5)
    add_member(parentAccount=ag_user, parentId=ag_id)

    _, ssh_report = teamlist.ag_team_list_search(searchValue=ssh_user)
    _, sh_report = teamlist.ag_team_list_search(searchValue=sh_user)
    _, ssma_report = teamlist.ag_team_list_search(searchValue=ssma_user)
    _, sma_report = teamlist.ag_team_list_search(searchValue=sma_user)
    _, ma_report = teamlist.ag_team_list_search(searchValue=ma_user)
    _, ag_report = teamlist.ag_team_list_search(searchValue=ag_user)
    verify_ag_team_list_search(ssh_report,
                                id=ssh_id,
                                account=ssh_user,
                                directDownLineCount=1,
                                downLinePlayerCount=6,
                                parentId=0)
    verify_ag_team_list_search(sh_report,
                                id=sh_id,
                                account=sh_user,
                                directDownLineCount=1,
                                downLinePlayerCount=5,
                                parentId=ssh_id)
    verify_ag_team_list_search(ssma_report,
                                id=ssma_id,
                                account=ssma_user,
                                directDownLineCount=1,
                                downLinePlayerCount=4,
                                parentId=sh_id)
    verify_ag_team_list_search(sma_report,
                                id=sma_id,
                                account=sma_user,
                                directDownLineCount=1,
                                downLinePlayerCount=3,
                                parentId=ssma_id)
    verify_ag_team_list_search(ma_report,
                                id=ma_id,
                                account=ma_user,
                                directDownLineCount=1,
                                downLinePlayerCount=2,
                                parentId=sma_id)
    verify_ag_team_list_search(ag_report,
                                id=ag_id,
                                account=ag_user,
                                directDownLineCount=0,
                                downLinePlayerCount=1,
                                parentId=ma_id)


def verify_ag_team_list_search(report,
                                id,
                                account,
                                directDownLineCount,
                                downLinePlayerCount,
                                parentId):
    log('Verify ag team list search.')
    report = report['data'][0]

    pytest.assume(report['id'] == id)
    pytest.assume(report['account'] == account)
    pytest.assume(report['directDownLineCount'] == directDownLineCount)
    pytest.assume(report['downLinePlayerCount'] == downLinePlayerCount)
    pytest.assume(report['status'] == 1)
    pytest.assume(report['updater'] == 'wellyadmin')
    pytest.assume(report['remark'] is None)
    pytest.assume(report['parentId'] == parentId)



def spend_time(func):
    def wrap(*args, **kwargs):
        start = time.time()
        value = func(*args, **kwargs)
        end = time.time()
        log(end-start)

        return value
    return wrap


def get_parent_id(account):

    get_level = teamlist.get_level(account=account)
    id = [id['id']
          for id in get_level
          if id['account'] == account]

    if len(id) == 0:
        raise ValueError(f"Id have nothing to get")


    return id[0]


def new_player_with_not_repeat():
    string = 'abcdefghujklmnopqrstuvwxyz1234567890'
    new_user =  'add' + ''.join(random.sample(string, 10))
    _, players = player.players_list_lookup(username=new_user)
    while len(players) != 0:
        _, players = player.players_list_lookup(username=new_user)

    with open('player.txt', 'a') as f:
        print(new_user, file=f)

    log(f'New player: {new_user}')
    return new_user


@spend_time
def new_agent_with_not_repeat(level_name):
    string = 'abcdefghujklmnopqrstuvwxyz1234567890'
    new_agent =  level_name + ''.join(random.sample(string, 12))

    _, ag_team_list_search = teamlist.ag_team_list_search(searchValue=new_agent)
    while ag_team_list_search['total'] != 0 and len(ag_team_list_search['data']) != 0:
        _, ag_team_list_search = teamlist.ag_team_list_search(searchValue=new_agent)

    with open('agent.txt', 'a') as f:
        print(new_agent, file=f)

    log(f"New agent: {new_agent}")
    return new_agent


def add_agent_and_return_agent_info(level_name, parentAccount, parentId, level):
    global user
    try:
        user = new_agent_with_not_repeat(level_name=level_name)
        _, add_agent = teamlist.add_agent(account=user,
                                          parentAccount=parentAccount,
                                          parentId=parentId,
                                          level=level)
    except ValueError as e:
        if str(e) == 'Expecting value: line 1 column 1 (char 0)':
            pass
        else:
            raise ValueError(str(e))

    user_id = get_parent_id(account=user)
    log(f"User: {user}\nUserId: {user_id}")
    return user, user_id


def add_member(parentAccount, parentId):
    new_player = new_player_with_not_repeat()
    try:
        teamlist.add_member(playerId=new_player, parentAccount=parentAccount, parentId=parentId)
    except ValueError as e:
        if str(e) == 'Expecting value: line 1 column 1 (char 0)':
            pass
        else:
            raise ValueError(f"Unknown error")

    return new_player
