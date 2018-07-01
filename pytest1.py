from test_function import solve_dict


def test_more_keys():
    assert solve_dict(keys=['a', 'b', 'c', 'd'], values=[1, 2]) == {'a': 1, 'b': 2, 'c': None, 'd': None}

def test_more_values():
    assert solve_dict(keys=['a', 'b'], values=[1, 2, 3, 4]) == {'a': 1, 'b': 2}

def test_zero_dict():
    assert solve_dict(keys=[], values=[]) == {}

def test_normal_dict():
    assert solve_dict(keys=['a', 'b', 'c'], values=[1, 2, 3]) == {'a': 1, 'b': 2, 'c': 3}
