import sys
import pytest
import allure
sys.path.append('..')
from base.base_player_resource import PlayerResource
from subprocess import call

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
def test_login(username='wellyadmin', status=right_status):

    code, res = player.login(username)
    pytest.assume(code == status)
    pytest.assume(res['needactivation'] is False)
    pytest.assume(res['verifytype'] == 'none')
    pytest.assume(res['token'] is not None)
    pytest.assume(res['settle'] is False)


@allure.feature('Login')
@allure.story('Minus')
@allure.step('')
@pytest.mark.Login
def test_login_with_null_and_error_username(usernames=['', '  ', '!@#', '我的天', str('w'*30)], status=wrong_status):

    for username in usernames:
        code, res = player.login(username)
        if username == usernames[0]:

            pytest.assume(code == status)
            pytest.assume(res['code'] == 0)
            pytest.assume(res['msg'] == 'userid is not provided')
            pytest.assume(res['replace'] is replace_None)

        else:
            pytest.assume(code == status)
            pytest.assume(res['code'] == 1)
            pytest.assume(res['msg'] == 'userid or password is incorrect')
            pytest.assume(res['replace'] is replace_None)


@allure.feature('Login')
@allure.story('Minus')
@allure.step('')
@pytest.mark.Login
def test_login_with_null_and_error_password(username='wellyadmin', pwds=['', '  ', '!@#', '我的天', str('w'*30)], status=wrong_status):

    for pwd in pwds:
        code, res = player.login(username, pwd)

        if pwd == pwds[0]:
            pytest.assume(code == status)
            pytest.assume(res['code'] == 0)
            pytest.assume(res['msg'] == 'password is not provided')
            pytest.assume(res['replace'] is replace_None)

        else:
            print('status')
            pytest.assume(code == status)
            pytest.assume(res['code'] == 1)
            pytest.assume(res['msg'] == 'userid or password is incorrect')
            pytest.assume(res['replace'] is replace_None)


@allure.feature('Player list')
@allure.story('Positive')
@allure.step('')
@pytest.mark.PlayerList
def test_player_list_search(languages=['ji3', ' ', '@#$', str('2'*30)], status=wrong_status):

    for language in languages:
        if language != languages[1]:
            status_code, response = player.players_list_search(language)
            pytest.assume(status_code == status)
            pytest.assume(response['code'] == 0)
            pytest.assume(f'nested exception is java.lang.NumberFormatException: '
                          f'For input string: "222222222222222222222222222222"' in response['msg'])
            pytest.assume(response['replace'] == replace_None)

        else:
            try:
               player.players_list_search(language)
            except Exception as e:
                log(e)
                pytest.assume(str(e) == 'Expecting value: line 1 column 1 (char 0)')




if __name__ == '__main__':
    call(['pytest', '-vs'])