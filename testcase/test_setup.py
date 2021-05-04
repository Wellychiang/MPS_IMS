import pytest
from . import teamlist


@pytest.mark.run(order=1)
def test_setup():
    _, response = teamlist.ims_login()
    teamlist.user_roles_setting(token=response)

