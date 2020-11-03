import sys
import pytest
import allure

sys.path.append('..')
from base.base_player_resource import PlayerResource
from pprint import pprint
import time
from datetime import datetime, timezone

env = 'stg'

player = PlayerResource(env)
log = player.log.info

right_status = 200
wrong_status = 498

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
def test_player_list_search_success_with_fuzzy_search(playerid: 'fixedwade' = 'wade',
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
        pytest.assume('wade0' in data['playerid'])
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
def test_player_list_search_success_with_sort(playerid='wade', sorts=('ASC', 'DESC'), status=right_status):

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

            names_num = 4
            for num in range(3):
                names_num -= 1
                pytest.assume(response['data'][num]['playerid'] == f'wade0{names_num}')


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

        pytest.assume(limit == len(response['data']))


@allure.feature('Player list')
@allure.story('Positive')
@allure.step('createdtstart = 10.1, end = 11.1.23:59')
@pytest.mark.PlayerList
def test_player_list_search_success_with_createtime_and_logintime(createdtstart=1601510400000,
                                                                  createdtend=1604275140000,
                                                                  playerid=None,
                                                                  switch_create=True,
                                                                  status=right_status):

    # createdtstart = int(datetime(2020, 10, 1, 0, 0, tzinfo=timezone.utc).timestamp() * 1000)
    # createdtend = int(datetime(2020, 11, 1, 23, 59, tzinfo=timezone.utc).timestamp() * 1000)
    status_code, response = player.players_list_search(createdtstart=createdtstart, createdtend=createdtend,
                                                       playerid=playerid, switch_create=switch_create)
    pytest.assume(response['total'] == 74)
    log(f'\n{response["total"]}')

    status_code, response = player.players_list_search(createdtstart=createdtstart, createdtend=createdtend,
                                                       playerid=playerid, switch_create=False)
    pytest.assume(response['total'] == 3127)
    log(f'\n{response["total"]}')


@allure.feature('Player list')
@allure.story('Positive')
@allure.step('All search will minus one if offset equal one')
@pytest.mark.PlayerList
def test_player_list_search_success_with_offset(playerids=('welly', 'wade'), offset=1, status=right_status):

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
@allure.step('Just verify this single api')
@pytest.mark.PlayerList
def test_player_list_search_success_with_different_sort_column(playerid='wade', sortcolumns=('playerid', 'firstname',
                                                                                             'viplevel', 'currency',
                                                                                             'createdate', 'city',
                                                                                             'agentid','totalavailable',
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
@allure.step('')
@pytest.mark.PlayerList
def test_player_list_search_success_with_total_available_from_and_to(createdtstart=1601510400000,
                                                                     createdtend=1604275140000,
                                                                     playerid=None, totalseriesfrom=1,
                                                                     totalseriesto=100, status=right_status):

    status_code, response = player.players_list_search(playerid=playerid, totalavailablefrom=totalseriesfrom,
                                                       totalavailableto=totalseriesto, createdtstart=createdtstart,
                                                       createdtend=createdtend, switch_create=False)
    log(f'response: {response["total"]}')
    pytest.assume(status_code, status)
    pytest.assume(response['total'] == 12)

    status_code, response = player.players_list_search(playerid=playerid, totaldepositfrom=totalseriesfrom,
                                                       totaldepositto=totalseriesto, createdtstart=createdtstart,
                                                       createdtend=createdtend, switch_create=False)
    log(f'response: {response["total"]}')
    pytest.assume(status_code, status)
    pytest.assume(response['total'] == 12)

    status_code, response = player.players_list_search(playerid=playerid, totalwithdrawalfrom=totalseriesfrom,
                                                       totalwithdrawalto=totalseriesto, createdtstart=createdtstart,
                                                       createdtend=createdtend, switch_create=False)
    log(f'response: {response["total"]}')
    pytest.assume(status_code, status)
    pytest.assume(response['total'] == 3)


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


if __name__ == '__main__':
    pass
