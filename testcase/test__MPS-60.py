from . import pytest
from . import allure
from . import teamlist
from . import player
from . import log
from . import base
from . import re
import time


@allure.feature('Team list in agent team')
@allure.story('Authority test with view only admin.')
@allure.step('')
@pytest.mark.skip("Just restrict frontend, this case need to change to gui")
def test_authority(username='wellyview'):
    teamlist.add_agent(username=username, account='add12787')
