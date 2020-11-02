import sys
import pytest
import allure

sys.path.append('..')
from base.base_player_resource import PlayerResource
from pprint import pprint

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
def test_login_with_null_and_error_username(usernames=['', '  ', '!@#', '我的天', str('w' * 60)], status=wrong_status):
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
def test_login_with_null_and_error_password(username='wellyadmin', pwds=['', '  ', '!@#', '我的天', str('w' * 60)],
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
@allure.step('')
@pytest.mark.PlayerList
def test_player_list_search_success_with_fuzzy_search_and_check_all_response(playerid: 'fixedwade' = 'wade', status=right_status):
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
            print(f'\nwade02\n')
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
            print(f'\nwade01\n')
            pytest.assume(data['mobile'] == '86 13131313142')
            pytest.assume(data['createdate'] == 1604287116460)

        elif data['playerid'] == 'wade03':
            print(f'\nwade03\n')
            pytest.assume(data['mobile'] == '86 13131313143')
            pytest.assume(data['createdate'] == 1604287141311)

        else:
            raise ValueError(f"It cant output without wade, or input without wade")

    for data in response['data']:
        if data['playerid'] == 'wade01' or data['playerid'] == 'wade03':
            print(f'\nwade01 and 03333333\n')
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
def test_player_list_search_success_with_exact_search(playerids=['wade01', 'welly', 'wade03'], playeridexactmatch=True, status=right_status):

    for playerid in playerids:
        status_code, response = player.players_list_search(playerid=playerid, playeridexactmatch=playeridexactmatch)
        pytest.assume(status_code == status)
        pytest.assume(response['total'] == 1)
        pytest.assume(response['total'] == len(response['data']))
        pytest.assume(response['data'][0]['playerid'] == playerid)


@allure.feature('Player list')
@allure.story('Positive')
@allure.step('')
@pytest.mark.PlayerList
def test_player_list_search_success_with_sort_desc_and_asc(playerid='wade', sort='DESC', status=right_status):

    status_code, response = player.players_list_search(playerid=playerid)
    # default ASC's sort
    pytest.assume(status_code, status)
    pytest.assume(response['data'][0]['playerid'] == 'wade01')
    pytest.assume(response['data'][1]['playerid'] == 'wade02')
    pytest.assume(response['data'][2]['playerid'] == 'wade03')

    status_code, response = player.players_list_search(playerid=playerid, sort=sort)
    # DESC's sort
    pytest.assume(status_code, status)
    pytest.assume(response['data'][0]['playerid'] == 'wade03')
    pytest.assume(response['data'][1]['playerid'] == 'wade02')
    pytest.assume(response['data'][2]['playerid'] == 'wade01')


@allure.feature('Player list')
@allure.story('Minus')
@allure.step('')
@pytest.mark.PlayerList
def test_player_list_with_null_and_wrong_languages(languages=['English', ' ', '@#$', str('2' * 30), '中文'], status=wrong_status):
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
@allure.story('Minus')
@allure.step('')
@pytest.mark.PlayerLis
def test_player_list_with_how_many_data_in_one_page(playerid=None, offset=None):
    status_code, response = player.players_list_search(offset=offset, playerid=playerid, limit=2000)

    print(len(response['data']))
    # for i in response['data']:
    #     print(f'\n{i}\n')


if __name__ == '__main__':
    pass
