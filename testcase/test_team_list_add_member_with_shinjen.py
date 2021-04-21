from . import pytest
from . import allure
from . import teamlist
from . import player
from . import log
from . import base
from . import re
import time


@allure.feature("Scenario for shinjen button in team list")
@pytest.mark.s
def test_shinjen_button(ssh_user="sshadd0000",
                        sh_user='shadd0000',
                        ssma_user='ssmaadd0000',
                        sma_user='smaadd0000',
                        ma_user='maadd0000',
                        ag_user='agadd0000',
                        playerId="add0000",
                        ):

    ssh_user, ssh_id = add_agent_and_return_agent_info(agentId=ssh_user, parentAccount=None, parentId=0, level=1)
    add_member(playerId, parentAccount=ssh_user, parentId=ssh_id)
    _, ssh_report = teamlist.ag_team_list(searchValue=ssh_user)
    verify_ag_team_list(ssh_report,
                        id=ssh_id,
                        account=ssh_user,
                        directDownLineCount=0,
                        downLinePlayerCount=1,
                        parentId=0)

    sh_user, sh_id = add_agent_and_return_agent_info(agentId=sh_user, parentAccount=ssh_user, parentId=ssh_id, level=2)
    add_member(playerId, parentAccount=sh_user, parentId=sh_id)
    _, ssh_report = teamlist.ag_team_list(searchValue=ssh_user)
    _, sh_report = teamlist.ag_team_list(searchValue=sh_user)
    verify_ag_team_list(ssh_report,
                        id=ssh_id,
                        account=ssh_user,
                        directDownLineCount=1,
                        downLinePlayerCount=2,
                        parentId=0)
    verify_ag_team_list(sh_report,
                        id=sh_id,
                        account=sh_user,
                        directDownLineCount=0,
                        downLinePlayerCount=1,
                        parentId=ssh_id)

    ssma_user, ssma_id = add_agent_and_return_agent_info(agentId=ssma_user, parentAccount=sh_user, parentId=sh_id, level=3)
    add_member(playerId, parentAccount=ssma_user, parentId=ssma_id)
    _, ssh_report = teamlist.ag_team_list(searchValue=ssh_user)
    _, sh_report = teamlist.ag_team_list(searchValue=sh_user)
    _, ssma_report = teamlist.ag_team_list(searchValue=ssma_user)
    verify_ag_team_list(ssh_report,
                        id=ssh_id,
                        account=ssh_user,
                        directDownLineCount=1,
                        downLinePlayerCount=3,
                        parentId=0)
    verify_ag_team_list(sh_report,
                        id=sh_id,
                        account=sh_user,
                        directDownLineCount=1,
                        downLinePlayerCount=2,
                        parentId=ssh_id)
    verify_ag_team_list(ssma_report,
                        id=ssma_id,
                        account=ssma_user,
                        directDownLineCount=0,
                        downLinePlayerCount=1,
                        parentId=sh_id)

    sma_user, sma_id = add_agent_and_return_agent_info(agentId=sma_user, parentAccount=ssma_user, parentId=ssma_id, level=4)
    add_member(playerId, parentAccount=sma_user, parentId=sma_id)
    _, ssh_report = teamlist.ag_team_list(searchValue=ssh_user)
    _, sh_report = teamlist.ag_team_list(searchValue=sh_user)
    _, ssma_report = teamlist.ag_team_list(searchValue=ssma_user)
    _, sma_report = teamlist.ag_team_list(searchValue=sma_user)
    verify_ag_team_list(ssh_report,
                        id=ssh_id,
                        account=ssh_user,
                        directDownLineCount=1,
                        downLinePlayerCount=4,
                        parentId=0)
    verify_ag_team_list(sh_report,
                        id=sh_id,
                        account=sh_user,
                        directDownLineCount=1,
                        downLinePlayerCount=3,
                        parentId=ssh_id)
    verify_ag_team_list(ssma_report,
                        id=ssma_id,
                        account=ssma_user,
                        directDownLineCount=1,
                        downLinePlayerCount=2,
                        parentId=sh_id)
    verify_ag_team_list(sma_report,
                        id=sma_id,
                        account=sma_user,
                        directDownLineCount=0,
                        downLinePlayerCount=1,
                        parentId=ssma_id)
    ma_user, ma_id = add_agent_and_return_agent_info(agentId=ma_user, parentAccount=sma_user, parentId=sma_id, level=5)
    add_member(playerId, parentAccount=ma_user, parentId=ma_id)
    _, ssh_report = teamlist.ag_team_list(searchValue=ssh_user)
    _, sh_report = teamlist.ag_team_list(searchValue=sh_user)
    _, ssma_report = teamlist.ag_team_list(searchValue=ssma_user)
    _, sma_report = teamlist.ag_team_list(searchValue=sma_user)
    _, ma_report = teamlist.ag_team_list(searchValue=ma_user)
    verify_ag_team_list(ssh_report,
                        id=ssh_id,
                        account=ssh_user,
                        directDownLineCount=1,
                        downLinePlayerCount=5,
                        parentId=0)
    verify_ag_team_list(sh_report,
                        id=sh_id,
                        account=sh_user,
                        directDownLineCount=1,
                        downLinePlayerCount=4,
                        parentId=ssh_id)
    verify_ag_team_list(ssma_report,
                        id=ssma_id,
                        account=ssma_user,
                        directDownLineCount=1,
                        downLinePlayerCount=3,
                        parentId=sh_id)
    verify_ag_team_list(sma_report,
                        id=sma_id,
                        account=sma_user,
                        directDownLineCount=1,
                        downLinePlayerCount=2,
                        parentId=ssma_id)
    verify_ag_team_list(ma_report,
                        id=ma_id,
                        account=ma_user,
                        directDownLineCount=0,
                        downLinePlayerCount=1,
                        parentId=sma_id)

    ag_user, ag_id = add_agent_and_return_agent_info(agentId=ag_user, parentAccount=ma_user, parentId=ma_id, level=5)
    add_member(playerId, parentAccount=ag_user, parentId=ag_id)

    _, ssh_report = teamlist.ag_team_list(searchValue=ssh_user)
    _, sh_report = teamlist.ag_team_list(searchValue=sh_user)
    _, ssma_report = teamlist.ag_team_list(searchValue=ssma_user)
    _, sma_report = teamlist.ag_team_list(searchValue=sma_user)
    _, ma_report = teamlist.ag_team_list(searchValue=ma_user)
    _, ag_report = teamlist.ag_team_list(searchValue=ag_user)
    verify_ag_team_list(ssh_report,
                        id=ssh_id,
                        account=ssh_user,
                        directDownLineCount=1,
                        downLinePlayerCount=6,
                        parentId=0)
    verify_ag_team_list(sh_report,
                        id=sh_id,
                        account=sh_user,
                        directDownLineCount=1,
                        downLinePlayerCount=5,
                        parentId=ssh_id)
    verify_ag_team_list(ssma_report,
                        id=ssma_id,
                        account=ssma_user,
                        directDownLineCount=1,
                        downLinePlayerCount=4,
                        parentId=sh_id)
    verify_ag_team_list(sma_report,
                        id=sma_id,
                        account=sma_user,
                        directDownLineCount=1,
                        downLinePlayerCount=3,
                        parentId=ssma_id)
    verify_ag_team_list(ma_report,
                        id=ma_id,
                        account=ma_user,
                        directDownLineCount=1,
                        downLinePlayerCount=2,
                        parentId=sma_id)
    verify_ag_team_list(ag_report,
                        id=ag_id,
                        account=ag_user,
                        directDownLineCount=0,
                        downLinePlayerCount=1,
                        parentId=ma_id)


def verify_ag_team_list(report,
                        id,
                        account,
                        directDownLineCount,
                        downLinePlayerCount,
                        parentId):

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


def new_player_with_not_repeat(playerId):
    _, players = player.players_list_lookup(username=playerId)
    if len(players) == 0:
        log(f'New playerId: {playerId}')
        return playerId

    add_players_info = [data[3:8]
                        for data in players
                        if playerId in data]

    if len(add_players_info) == 0:
        raise ValueError("Add player's info error, info shouldn't equal 0.")

    playerId = re.sub('[0-9]', '', playerId)
    if int(max(add_players_info)) + 1 >= 10:
        next_new_player = playerId + '000' + str(int(max(add_players_info)) + 1)
    else:
        next_new_player = playerId + '0000' + str(int(max(add_players_info)) + 1)

    return new_player_with_not_repeat(next_new_player)


@spend_time
def new_agent_with_not_repeat(agentId):
    _, ag_team_list = teamlist.ag_team_list(searchValue=agentId)

    add_ag_info = [data['account'][-4:]
                   for data in ag_team_list['data']
                   if agentId in data['account']]

    if len(add_ag_info) == 0:
        raise ValueError("Add agent's info error, info shouldn't equal 0.")

    next_new_ag = agentId + str(int(max(add_ag_info)) + 1)
    log(f"New agent: {next_new_ag}")

    return next_new_ag


def add_agent_and_return_agent_info(agentId, parentAccount, parentId, level):
    try:
        user = new_agent_with_not_repeat(agentId=agentId)
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


def add_member(player_id, parentAccount, parentId):
    new_player = new_player_with_not_repeat(player_id)
    try:
        teamlist.add_member(playerId=new_player, parentAccount=parentAccount, parentId=parentId)
    except ValueError as e:
        if str(e) == 'Expecting value: line 1 column 1 (char 0)':
            pass
        else:
            raise ValueError(f"Unknown error")

    return new_player
