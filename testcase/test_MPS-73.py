from . import pytest
from . import allure
from . import teamlist
from . import player
from . import log
from . import base
from . import re
import time


@allure.feature('Team list in agent team')
@allure.story('Scenario with change agent status and verify.')
@allure.step('')
def test_verify_status_with_ag_team_list(username='add111',
                                           values=(3, 1, 2),
                                           login_status=(498, 200, 498)):
    """
    Missing login user get kicked verify, it should be in gui mode.
    """
    global user_id
    _, list_data = teamlist.ag_team_list_search(searchValue=username)

    lists_data = list_data['data']
    for list_data in lists_data:
        if 'add111' in list_data['account']:
            user_id = list_data['id']
        else:
            raise ValueError('Search failed')

    for i in range(3):
        teamlist.agent_status_update(ag_id=user_id, value=values[i])
        status_code = teamlist.agentSite_login(username=username)
        pytest.assume(status_code == login_status[i])
