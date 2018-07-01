import pytest

from test_function import solve_dict


@pytest.mark.parametrize('keys,values,result', [
    (['a', 'b', 'c', 'd'], [1, 2], {'a': 1, 'b': 2, 'c': None, 'd': None}),
    (['a', 'b'], [1, 2, 3, 4], {'a': 1, 'b': 2}),
    ([], [], {}),
    (['a', 'b', 'c'], [1, 2, 3], {'a': 1, 'b': 2, 'c': 3})
])
def test_it(keys, values, result):
    assert solve_dict(keys=keys, values=values) == result
