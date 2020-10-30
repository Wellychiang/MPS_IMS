import pytest
import os


if __name__ == '__main__':
    pytest.main(['-vsm', 'PlayerList'])
    # os.system('del /q report')
    # pytest.main(['-vs', '--alluredir', 'report'])
