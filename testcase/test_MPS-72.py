from . import pytest
from . import allure
from . import teamlist
from . import player
from . import log
from . import base
from . import re
import time


@allure.feature()
@allure.story()
@allure.step('')
@pytest.mark.skip('Wait for the specification.')
def test_dd(username='089457',
            point=10000):
    month = time.localtime(time.time())[1]
    day = time.localtime(time.time())[2]
    start_time, end_time = base.start_and_end_time(start_m=month,
                                                   start_d=day,
                                                   end_m=month,
                                                   end_d=day)
    global userid

    _, ag_team_list = teamlist.ag_team_list_search(searchValue=username)
    list_datas = ag_team_list['data']
    for list_data in list_datas:
        if list_data['account'] == username:
            userid = list_data['id']
            o_point = list_data['point']

    teamlist.agent_point(method='PUT',
                         point=12345678901234567,
                         txn_type='ADD',
                         down_line_id=userid)

    # _, response = teamlist.agent_point(method='GET',
    #                                    start=start_time,
    #                                    end=end_time)
    # for data in response['data']:
    #     print(data)




