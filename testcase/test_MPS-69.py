from . import pytest
from . import allure
from . import teamlist
from . import player
from . import log
from . import base
from . import re
import time


@allure.feature()
@allure.step('')
@pytest.mark.d
def test_search_function(username='ssh001',
                         updater='UPDATER'):
    _, response = teamlist.ag_team_list(searchValue=username)

    lists_data = response['data']
    for list_data in lists_data:
        assert username in list_data['account']


    _, response = teamlist.ag_team_list(searchValue='crystal',
                                        searchField=updater,)
