import pytest
import os


if __name__ == '__main__':
    pytest.main(['-vvsm', 'Playerid'])

    # os.system('del /q report')
    # pytest.main(['-vvs', '--alluredir', 'report'])
    # pytest.main(['-vvsm', 'PlayerLis', '--alluredir', 'report'])
