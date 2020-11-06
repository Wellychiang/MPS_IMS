import pytest
import allure
from base.base_player_resource import PlayerResource
import json
from pprint import pprint
import time
from datetime import datetime, timezone


env = 'stg'

# 改成執行時選定環境
player = PlayerResource(env)
log = player.log.info

right_status = 200
wrong_status = 498
put_status = 204

# login
replace_None = None


@allure.feature('Login')
@allure.story('Positive')
@allure.step('')
@pytest.mark.Login
def test_login_success(username='wellyadmin', status=right_status):
    status_code, response = player.login(username)

    pytest.assume(status_code == status)
    pytest.assume(response['needactivation'] is False)
    pytest.assume(response['verifytype'] == 'none')
    pytest.assume(response['token'] is not None)
    pytest.assume(response['settle'] is False)


@allure.feature('Login')
@allure.story('Minus')
@allure.step('')
@pytest.mark.Login
def test_login_with_null_username_and_password(username='', pwd='', status=wrong_status):

    status_code, response = player.login(username, pwd)
    pytest.assume(status_code == status)
    pytest.assume(response['code'] == 0)
    pytest.assume(response['msg'] == 'userid is not provided')
    pytest.assume(response['replace'] is replace_None)


@allure.feature('Login')
@allure.story('Minus')
@allure.step('')
@pytest.mark.Login
def test_login_with_null_and_error_username(usernames=('', '  ', '!@#', '我的天', str('w' * 60)), status=wrong_status):
    for username in usernames:
        status_code, response = player.login(username)
        if username == usernames[0]:
            pytest.assume(status_code == status)
            pytest.assume(response['code'] == 0)
            pytest.assume(response['msg'] == 'userid is not provided')
            pytest.assume(response['replace'] is replace_None)

        else:
            pytest.assume(status_code == status)
            pytest.assume(response['code'] == 1)
            pytest.assume(response['msg'] == 'userid or password is incorrect')
            pytest.assume(response['replace'] is replace_None)


@allure.feature('Login')
@allure.story('Minus')
@allure.step('')
@pytest.mark.Login
def test_login_with_null_and_error_password(username='wellyadmin', pwds=('', '  ', '!@#', '我的天', str('w' * 60)),
                                            status=wrong_status):
    for pwd in pwds:
        status_code, response = player.login(username, pwd)

        if pwd == pwds[0]:
            pytest.assume(status_code == status)
            pytest.assume(response['code'] == 0)
            pytest.assume(response['msg'] == 'password is not provided')
            pytest.assume(response['replace'] is replace_None)

        else:
            pytest.assume(status_code == status)
            pytest.assume(response['code'] == 1)
            pytest.assume(response['msg'] == 'userid or password is incorrect')
            pytest.assume(response['replace'] is replace_None)


@allure.feature('Player list')
@allure.story('Positive')
@allure.step('Fuzzy search with all response verify')
@pytest.mark.PlayerList
def test_player_list_search_success_with_fuzzy_search(playerid: 'fixedwade' = 'wade0',
                                                      status=right_status):
    status_code, response = player.players_list_search(playerid=playerid)

    pytest.assume(status_code == status)
    pytest.assume(response['total'] == len(response['data']))
    pytest.assume(response['total'] == 3)

    # wade02斷言自己的, 其餘wade帳號皆用大多數同樣斷言
    # 兩個相同wade02不同: currency, firstname, vipid, totalavailable, viplevel, vipgroupid, levelname, totaldeposit,
    # totaldepositcount, vgname, banksnameaccount,

    # 各不相同: mobile, createdate
    # skip: logintime
    for data in response['data']:
        pytest.assume(playerid in data['playerid'])
        pytest.assume(data['lastname'] is None)
        pytest.assume(data['im1'] is None)
        pytest.assume(data['im2'] is None)
        pytest.assume(data['status'] == 1)
        pytest.assume(data['tagnames'] == 'SameIP')
        pytest.assume(data['agentid'] is None)
        pytest.assume(data['hasverifiedmobile'] is False)
        pytest.assume(data['displayname'] is None)
        pytest.assume(data['ulagentid'] is None)
        pytest.assume(data['ulagentaccount'] is None)
        pytest.assume(data['totalwithdraw'] == 0.0)
        pytest.assume(data['totalwithdrawcount'] == 0)
        pytest.assume(data['affiliateupline'] == '')
        pytest.assume(data['uplinepoint'] is None)
        pytest.assume(data['createdatestr'] is None)
        pytest.assume(data['logintimestr'] is None)
        pytest.assume(data['statusstr'] is None)

        if data['playerid'] == 'wade02':
            log(f'\nwade02\n')
            pytest.assume(data['currency'] == 'CNY')
            pytest.assume(data['firstname'] == 'qweqww')
            pytest.assume(data['vipid'] == 'a582d64f-45e2-4769-94b3-2573b59279a3')
            pytest.assume(data['totalavailable'] == 10017.88)
            pytest.assume(data['viplevel'] == 3)
            pytest.assume(data['vipgroupid'] == '252ffc0e-b40e-4e72-8c75-c92677947ae7')
            pytest.assume(data['levelname'] == '3')
            pytest.assume(data['totaldeposit'] == 294.0)
            pytest.assume(data['totaldepositcount'] == 1)
            pytest.assume(data['vgname'] == '0130level-3')
            pytest.assume(data['banksnameaccount'] == 'eyny银行 - ji3jo12123ijzxcwe')

        elif data['playerid'] == 'wade01':
            log(f'\nwade01\n')
            pytest.assume(data['mobile'] == '86 13131313142')
            pytest.assume(data['createdate'] == 1604287116460)

        elif data['playerid'] == 'wade03':
            log(f'\nwade03\n')
            pytest.assume(data['mobile'] == '86 13131313143')
            pytest.assume(data['createdate'] == 1604287141311)

        else:
            raise ValueError(f"It can not output without wade1~3, or input without wade")

    for data in response['data']:
        if data['playerid'] == 'wade01' or data['playerid'] == 'wade03':
            log(f'\nwade01 and wade03\n')
            pytest.assume(data['currency'] == 'USD')
            pytest.assume(data['firstname'] is None)
            pytest.assume(data['vipid'] == '93f99682-37e9-4dbf-8805-f4061c37adae')
            pytest.assume(data['totalavailable'] == 0.0)
            pytest.assume(data['viplevel'] == 1)
            pytest.assume(data['vipgroupid'] == '27140498-febc-40fc-a830-dbcbd4446f6d')
            pytest.assume(data['levelname'] == 'Level 1')
            pytest.assume(data['totaldeposit'] == 0.0)
            pytest.assume(data['totaldepositcount'] == 0)
            pytest.assume(data['vgname'] == 'Default VIP Group - USD-Level 1')
            pytest.assume(data['banksnameaccount'] is None)


@allure.feature('Player list')
@allure.story('Positive')
@allure.step('')
@pytest.mark.PlayerList
def test_player_list_search_success_with_exact_search(playerids=('wade01', 'welly', 'wade03'),
                                                      playeridexactmatch=True,
                                                      status=right_status):

    for playerid in playerids:
        status_code, response = player.players_list_search(playerid=playerid, playeridexactmatch=playeridexactmatch)
        pytest.assume(status_code == status)
        pytest.assume(response['total'] == 1)
        pytest.assume(response['total'] == len(response['data']))
        pytest.assume(response['data'][0]['playerid'] == playerid)


@allure.feature('Player list')
@allure.story('Positive')
@allure.step("Verify DESC and ASC's order")
@pytest.mark.PlayerList
def test_player_list_search_success_with_sort(playerid='wade0', sorts=('ASC', 'DESC'), status=right_status):

    for sort in sorts:
        status_code, response = player.players_list_search(playerid=playerid, sort=sort)
        if sort == sorts[0]:
            # default ASC's sort
            pytest.assume(status_code == status)
            for num in range(3):
                pytest.assume(response['data'][num]['playerid'] == f'wade0{num+1}')

        else:
            # DESC's sort
            pytest.assume(status_code == status)

            # 以 response total 為基準, copy 出 wade 遞減時需要的數字並 + 1, 因遞減時的第一筆資料就會 -1
            names_num = int(response['total'])
            nums_copy_to_minus_one = names_num + 1
            for num in range(names_num):
                nums_copy_to_minus_one -= 1
                pytest.assume(response['data'][num]['playerid'] == f'wade0{nums_copy_to_minus_one}')


@allure.feature('Player list')
@allure.story('Minus')
@allure.step('')
@pytest.mark.PlayerList
def test_player_list_search_with_null_and_wrong_languages(languages=('English', ' ', '@#$', str('2' * 30), '中文'),
                                                          status=wrong_status):
    for language in languages:
        if language != languages[1]:
            status_code, response = player.players_list_search(language)
            pytest.assume(status_code == status)
            pytest.assume(response['code'] == 0)
            pytest.assume(f'nested exception is java.lang.NumberFormatException: For input string: "{language}"'
                          in response['msg'])
            pytest.assume(response['replace'] == replace_None)

        else:  # This is for '  '
            try:
                player.players_list_search(language)
            except Exception as e:
                log(e)
                pytest.assume(str(e) == 'Expecting value: line 1 column 1 (char 0)')


@allure.feature('Player list')
@allure.story('Positive')
@allure.step("Display the limit's number's info in one page")
@pytest.mark.PlayerList
def test_player_list_search_success_with_limit(playerid=None, limits=(25, 50, 100)):

    for limit in limits:
        status_code, response = player.players_list_search(playerid=playerid, limit=limit)

        log(f'{response["total"]}, {len(response["data"])}')
        pytest.assume(limit == len(response['data']))


@allure.feature('Player list')
@allure.story('Positive')
@allure.step('Verify time in time block, createdtstart = 10.1, end = 11.1.23:59')
@pytest.mark.PlayerList
def test_player_list_search_success_with_createtime_and_logintime(createdtstart=1601481600000,
                                                                  createdtend=1604246399999,
                                                                  playerid=None,
                                                                  switch_create=True,
                                                                  status=right_status):

    # createdtstart = int(datetime(2020, 10, 1, 0, 0, tzinfo=timezone.utc).timestamp() * 1000)
    # createdtend = int(datetime(2020, 11, 1, 23, 59, tzinfo=timezone.utc).timestamp() * 1000)
    status_code, response = player.players_list_search(createdtstart=createdtstart, createdtend=createdtend,
                                                       playerid=playerid, switch_create=switch_create)
    pytest.assume(status_code, status)
    pytest.assume(response['total'] == 74)

    # status_code, response = player.players_list_search(createdtstart=createdtstart, createdtend=createdtend,
    #                                                    playerid=playerid, switch_create=False)
    # # When switch_create=False, createstart will change to loginstart
    # pytest.assume(status_code, status)
    # pytest.assume(response['total'] != 100)


@allure.feature('Player list')
@allure.story('Positive')
@allure.step('All search will minus one if offset equal one')
@pytest.mark.PlayerList
def test_player_list_search_success_with_offset(playerids=('welly', 'wade'),
                                                offset=1,
                                                status=right_status):

    for playerid in playerids:
        status_code, response = player.players_list_search(playerid=playerid)
        origin_data_length = len(response['data'])

        status_code, response = player.players_list_search(playerid=playerid, offset=offset)
        offset_data_length = len(response['data'])

        log(f'\norigin_data_length: {len(response["data"])}\noffset_data_length: {offset_data_length}')

        pytest.assume(status_code, status)
        pytest.assume(int(origin_data_length) - 1 == int(offset_data_length))


@allure.feature('Player list')
@allure.story('Positive')
@allure.step('Choose which sortcolumns to sort')
@pytest.mark.PlayerList
def test_player_list_search_success_with_different_sort_column(playerid='wade', sortcolumns=('playerid',
                                                                                             'firstname',
                                                                                             'viplevel',
                                                                                             'currency',
                                                                                             'createdate',
                                                                                             'city',
                                                                                             'agentid',
                                                                                             'totalavailable',
                                                                                             'totaldeposit',
                                                                                             'totalwithdraw',
                                                                                             'logintime',
                                                                                             'status',
                                                                                             'totaldepositcount',
                                                                                             'totalwithdrawcount')):
    _, response = player.players_list_search(playerid=playerid)
    default_total = int(response['total'])

    for sortcolumn in sortcolumns:
        status_code, response = player.players_list_search(playerid=playerid, sortcolumn=sortcolumn)
        pytest.assume(response['total'] == len(response['data']))
        pytest.assume(int(response['total']) == default_total)


@allure.feature('Player list')
@allure.story('Positive')
@allure.step("This case contains available, deposit and withdrawl's total in a fixed time")
@pytest.mark.PlayerLis
def test_player_list_search_success_with_total_available_from_and_to(createdtstart=1601481600000,
                                                                     createdtend=1604246399999,
                                                                     playerid=None,
                                                                     totalseriesfrom=1,
                                                                     totalseriesto=100,
                                                                     status=right_status):

    status_code, response = player.players_list_search(playerid=playerid, totalavailablefrom=totalseriesfrom,
                                                       totalavailableto=totalseriesto, createdtstart=createdtstart,
                                                       createdtend=createdtend)
    pytest.assume(status_code, status)
    pytest.assume(response['total'] == 4)

    status_code, response = player.players_list_search(playerid=playerid, totaldepositfrom=totalseriesfrom,
                                                       totaldepositto=totalseriesto, createdtstart=createdtstart,
                                                       createdtend=createdtend)
    pytest.assume(status_code, status)
    pytest.assume(response['total'] == 8)

    status_code, response = player.players_list_search(playerid=playerid, totalwithdrawalfrom=totalseriesfrom,
                                                       totalwithdrawalto=totalseriesto, createdtstart=createdtstart,
                                                       createdtend=createdtend)
    pytest.assume(status_code, status)
    pytest.assume(response['total'] == 0)


@allure.feature('Player list')
@allure.story('Positive')
@allure.step('Real name column')
@pytest.mark.PlayerList
def test_player_list_search_success_with_first_name(firstnames=('welly', 'wade'), status=right_status):

    for firstname in firstnames:
        status_code, response = player.players_list_search(firstname=firstname)

        pytest.assume(status_code == status)
        if len(response["data"]) == 0:
            log(f'{firstname} is not a valid firstname')
        else:
            for data in response['data']:
                log(f'This loops firstname: {data["firstname"]}')
                pytest.assume(firstname in data['firstname'])


@allure.feature('Player list')
@allure.story('Positive')
@allure.step('Agent upline and agent team search in fixed time')
@pytest.mark.PlayerList
def test_player_list_search_success_with_agentupline(playerid=None,
                                                     agentidexactmatch=False,
                                                     agentuplines=('a', 'awell', 'b'),
                                                     status=right_status,
                                                     createdtstart=1601510400000,
                                                     createdtend=1604275140000,
                                                     ):
    # 模糊搜尋代理
    agent_count = {}
    for agentupline in agentuplines:
        status_code, response = player.players_list_search(playerid=playerid,
                                                           agentidexactmatch=agentidexactmatch,
                                                           agentupline=agentupline,
                                                           createdtstart=createdtstart,
                                                           createdtend=createdtend,
                                                           )
        # 初始化傳入的數值 = 0, 開始計數
        agent_count.setdefault(agentupline, 0)
        pytest.assume(status_code == status)
        if len(response['data']) != 0:
            agent_count[agentupline] += 1
            log(f'agent count: {agent_count}')
            for data in response['data']:
                pytest.assume(agentupline in data['agentid'])
        else:
            log('This is not a valid fuzzy input')

    pytest.assume(agent_count['a'] and agent_count['awell'] == 1)
    pytest.assume(agent_count['b'] == 0)

    # 準確搜尋代理
    status_code, response = player.players_list_search(playerid=playerid,
                                                       agentidexactmatch=True,
                                                       agentupline='awelly1')
    if response['total'] == 1:
        pytest.assume(status_code == status)
        pytest.assume(response['data'][0]['agentid'] == 'awelly1')

    else:
        raise ValueError(f'Response error: total: {response["total"]}\nagentid: {response["data"][0]["agentid"]}')

    # 準確和模糊搜尋代理團隊(bluecat團隊)
    agent_lines = ('bluecat', 'b')
    for agent_line in agent_lines:
        if agent_line == agent_lines[1]:
            exactmatch = False
        else:
            exactmatch = True
        status_code, response = player.players_list_search(playerid=playerid,
                                                           agentidexactmatch=exactmatch,
                                                           agentupline=agent_line,
                                                           ulagent=True,
                                                           createdtstart=createdtstart,
                                                           createdtend=1606751999999,
                                                           switch_create=False
                                                           )
        log(f'exactmatch: {exactmatch}')
        pytest.assume(status_code == status)
        pytest.assume(response['total'] == 1)
        pytest.assume(response['data'][0]['playerid'] == 'bcat02')
        pytest.assume(response['data'][0]['ulagentaccount'] == 'bluecat')


@allure.feature('Player list')
@allure.story('Positive')
@allure.step("welly4's laodieshin upline: welly")
@pytest.mark.PlayerList
def test_player_list_search_success_with_affiliateupline(playerid=None,
                                                         affiliateupline='welly',
                                                         status=right_status):

    status_code, response = player.players_list_search(playerid=playerid,
                                                       affiliateupline=affiliateupline)

    pytest.assume(status_code == status)
    pytest.assume(response['data'][0]['playerid'] == 'welly4')


@allure.feature('Player list')
@allure.story('Positive')
@allure.step("Search for bank account")
@pytest.mark.PlayerList
def test_player_list_search_success_with_bankaccount(playerid=None,
                                                     bankaccount=5767373481815,
                                                     status=right_status):

    status_code, response = player.players_list_search(playerid=playerid,
                                                       bankaccount=bankaccount)
    log(response['data'])
    pytest.assume(status_code == status)
    pytest.assume(response['total'] == 1)
    pytest.assume(response['data'][0]['playerid'] == '089457')
    pytest.assume(str(bankaccount) in response['data'][0]['banksnameaccount'])


@allure.feature('Player list')
@allure.story('Positive')
@allure.step("Verify the fixed status 1, 3, 4")
@pytest.mark.PlayerList
def test_player_list_search_success_with_status(playerid='wade', status=right_status):
    status_code, response = player.players_list_search(playerid=playerid)

    pytest.assume(status_code == status)

    if len(response['data']) != 0:
        for data in response['data']:
            print(data['playerid'], data['status'])
            if 'wade0' in data['playerid']:
                pytest.assume(data['status'] == 1)
            elif data['playerid'] == 'wade4':
                pytest.assume(data['status'] == 3)
            elif data['playerid'] == 'wade5':
                pytest.assume(data['status'] == 4)
            elif data['playerid'] == 'wade6':
                pytest.assume(data['status'] == 1)
            elif data['playerid'] == 'wade7':
                pytest.assume(data['status'] == 0)


@allure.feature('Player list')
@allure.story('Positive')
@allure.step("Verify the fixed mobile message verification with player welly")
@pytest.mark.PlayerList
def test_player_list_search_success_with_mobile_and_short_message_verify(playerid=None,
                                                                         mobile='86 13131313131',
                                                                         status=right_status,
                                                                         to_verify_mobile_message=(None, False, True)):
    # None 是短信驗證篩選全部, False 是篩選沒驗證的
    for verify_mobile in to_verify_mobile_message:
        if verify_mobile != to_verify_mobile_message[2]:
            status_code, response = player.players_list_search(playerid=playerid,
                                                               mobile=mobile,
                                                               hasverifiedmobile=verify_mobile)
            pytest.assume(status_code == status)
            pytest.assume(response['total'] == 1)
            pytest.assume(response['data'][0]['playerid'] == 'welly')
            pytest.assume(response['data'][0]['mobile'] == mobile)
        else:
            status_code, response = player.players_list_search(playerid=playerid,
                                                               mobile=mobile,
                                                               hasverifiedmobile=verify_mobile)
            pytest.assume(status_code == status)
            pytest.assume(response['total'] == 0)
            pytest.assume(len(response['data']) == 0)


@allure.feature('Player list')
@allure.story('Positive')
@allure.step("")
@pytest.mark.PlayerList
def test_player_list_search_success_with_vipid(playerid=None,
                                               vipid='e66fec49-5173-4389-9432-bb98a5f7b87f',
                                               status=right_status):

    status_code, response = player.players_list_search(playerid=playerid, vipid=vipid)

    pytest.assume(status_code == status)

    if len(response['data']) != 0:
        for data in response['data']:
            pytest.assume(data['vipid'] == vipid)

    else:
        raise ValueError('This vip id is None, plz change the other vipid')


@allure.feature('Player list')
@allure.story('Positive')
@allure.step("Verify the tags 'SameIP' with fixed time")
@pytest.mark.PlayerList
def test_player_list_search_success_with_tags(playerid=None,
                                              createdtstart=1601481600000,
                                              createdtend=1606751999999,
                                              tags='6ff786bb-4901-4b17-8b89-55dc3585b4d2',
                                              status=right_status):
    status_code, response = player.players_list_search(playerid=playerid,
                                                       createdtstart=createdtstart,
                                                       createdtend=createdtend,
                                                       tags=tags)

    pytest.assume(status_code == status)
    pytest.assume(response['total'] == 90)
    pytest.assume(response['data'][0]['tagnames'] == 'SameIP')


@allure.feature('Player list')
@allure.story('Positive')
@allure.step("Verify the email with fixed time")
@pytest.mark.PlayerList
def test_player_list_search_success_with_tags(playerid=None,
                                              createdtstart=1601481600000,
                                              createdtend=1606751999999,
                                              email='welly.chiang@nexiosoft.com',
                                              status=right_status):

    status_code, response = player.players_list_search(playerid=playerid,
                                                       createdtstart=createdtstart,
                                                       createdtend=createdtend,
                                                       email=email)
    pytest.assume(status_code == status)

    for data in response['data']:
        pytest.assume(data['email'] == email)


@allure.feature('Player list')
@allure.story('Positive')
@allure.step("Verify the IM with fixed time")
@pytest.mark.PlayerList
def test_player_list_search_success_with_IM1_and_IM2(playerid=None,
                                                     createdtstart=1601481600000,
                                                     createdtend=1606751999999,
                                                     im1='im1welly',
                                                     im2='im2welly',
                                                     status=right_status):

    status_code, response = player.players_list_search(playerid=playerid,
                                                       createdtstart=createdtstart,
                                                       createdtend=createdtend,
                                                       im1=im1)
    if response['total'] == 0:
        raise ValueError(f"im1: '{im1}' is lost")
    pytest.assume(status_code == status)
    pytest.assume(response['data'][0]['im1'] == im1)

    status_code, response = player.players_list_search(playerid=playerid,
                                                       createdtstart=createdtstart,
                                                       createdtend=createdtend,
                                                       im2=im2)
    if response['total'] == 0:
        raise ValueError(f"im2: '{im2}' is lost")
    pytest.assume(status_code == status)
    pytest.assume(response['data'][0]['im2'] == im2)


@allure.feature('Player list lookup')
@allure.story('Positive')
@allure.step("To register a new user, look up a similar username")
@pytest.mark.PlayerList
def test_player_list_lookup_success(username='welly', status=right_status):

    status_code, response = player.players_list_lookup(username)
    pytest.assume(status_code == status)
    pytest.assume(len(response) <= 10)

    for data in response:
        pytest.assume(username in data)


@allure.feature('Player')
@allure.story('Positive')
@allure.step("Register a new user")
@pytest.mark.Register
def test_player_success(username='welly', user_num=24, status=right_status):

    status_code, response = player.players(username, user_num)

    while status_code == wrong_status:
        if response['msg'] == 'the specified playerid has already been taken':
            user_num += 1
            status_code, response = player.players(username, user_num)
        else:
            raise ValueError(f'Response msg: {response["msg"]}')

    pytest.assume(status_code == status)
    pytest.assume(username in response['playerid'])


@allure.feature('Player id')
@allure.story('Positive')
@allure.step("User info compared")
@pytest.mark.PlayerId
def test_player_playerid_success(username='wade01', status=right_status):

    status_code, response = player.players_playerid(username)

    pytest.assume(status_code == status)

    with open('compared_json/playerid.json', 'w') as f:
        print(response, file=f)
    with open('compared_json/playerid.json', 'r') as f:
        clean_up = f.read().strip().split(',')
        playerid = clean_up

    # with open('original_playerid.json', 'w') as f:
    #     print(response, file=f)
    with open('compared_json/original_playerid.json', 'r') as f:
        # original_playerid = f.read()
        clean_up = f.read().strip().split(',')
        origin = clean_up

    print(playerid)
    assert origin == playerid


@allure.feature('Player status')
@allure.story('Positive')
@allure.step("Change status")
@pytest.mark.PlayerId
def test_player_playerid_status_success(username='wade6',
                                        statuses=(4, 3, 2, 0, 1),
                                        statuss=put_status):

    for status in statuses:
        status_code = player.players_playerid_status(username=username,
                                                     status=status,)
        assert status_code == statuss


@allure.feature('Player notes')
@allure.story('Positive')
@allure.step("User notes")
@pytest.mark.PlayerId
def test_player_playerid_notes_success(username='welly', notes='Who am i', status=put_status):

    status_code = player.players_playerid_notes(username, notes)

    assert status_code == status


@allure.feature('Player ')
@allure.story('Positive')
@allure.step("user info")
@pytest.mark.Transaction
def test_transaction_search(username='welly',
                            status=right_status,
                            endtxntime=1603209599999,
                            starttxntime=1602432000000):

    status_code, response = player.transactions_search(username,
                                                       starttxntime=starttxntime,
                                                       endtxntime=endtxntime)

    pytest.assume(status_code == status)

    with open('compared_json/transaction_search.json', 'w')as f:
        print(response, file=f)
    with open('compared_json/transaction_search.json', 'r')as f:
        clean_up = f.read().strip().split(',')
        transaction_search = clean_up

    # with open('compared_json/original_transaction_search.json', 'w')as f:
    #     print(response, file=f)
    with open('compared_json/original_transaction_search.json', 'r')as f:
        clean_up = f.read().strip().split(',')
        original_transaction_search = clean_up

    assert original_transaction_search == transaction_search


if __name__ == '__main__':
    pass
