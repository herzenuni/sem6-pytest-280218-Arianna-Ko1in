from hypothesis import given
from hypothesis.strategies import dictionaries, lists, characters, integers, one_of, none, nothing

from test_function import solve_dict


@given(
    x=lists(one_of(integers(),characters()),unique=True),
    y=lists(one_of(integers(),characters())))

def test_it(x, y):
    z = solve_dict(keys=x, values=y)
    assert len(z.keys())==len(x)
    for (i,key) in enumerate(x):
        assert list(z.keys())[i]==x[i]
        if i>=len(y):
            assert z[key] is None
        else:
            assert z[key]==y[i]

test_it()
