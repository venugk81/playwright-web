import pytest


@pytest.mark.parametrize("value", [1, 3, 5, 6, 7, 4.5])
def test_method(value):
    print(f"-------Value-------: {value}")
    assert isinstance(value, int), "Not a integer value"



# pytest_param/test_SingleParam.py::test_method[1]
# pytest_param/test_SingleParam.py::test_method[3]
# pytest_param/test_SingleParam.py::test_method[5]
# pytest_param/test_SingleParam.py::test_method[6]
# pytest_param/test_SingleParam.py::test_method[7]
# pytest_param/test_SingleParam.py::test_method[4.5]
#
# ========================= 1 failed, 5 passed in 0.02s ==========================
# PASSED                       [ 16%]-------Value-------: 1
# PASSED                       [ 33%]-------Value-------: 3
# PASSED                       [ 50%]-------Value-------: 5
# PASSED                       [ 66%]-------Value-------: 6
# PASSED                       [ 83%]-------Value-------: 7
# FAILED                     [100%]-------Value-------: 4.5