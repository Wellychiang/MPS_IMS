import pytest
import os


if __name__ == '__main__':
    # pytest.main(['-vvsm', 'n'])

    # pytest.main(['-vvs'])

    # os.system('del /q report')
    pytest.main(['-vvs', '--alluredir', 'report'])   # 調試完記得開這行就好
    # pytest.main(['-vvsm', 'PlayerLis', '--alluredir', 'report'])
