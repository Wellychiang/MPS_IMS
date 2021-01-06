import pytest


if __name__ == '__main__':
    # pytest.main(['-vvsm', 'd'])

    # pytest.main(['-vvs'])

    pytest.main(['-vvs', '--reruns', '2', '--alluredir', 'report'])   # 調試完記得開這行就好
