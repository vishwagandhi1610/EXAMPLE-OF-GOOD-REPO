import arithmatic


def test_calc_addition():
    output = arithmatic.add(2, 4)
    assert output == 6


def test_calc_substraction():
    output = arithmatic.sub(12, 4)
    assert output == 8


def test_calc_multiply():
    output = arithmatic.mul(6, 4)
    assert output == 24


def test_calc_divide():
    output = arithmatic.div(10, 2)
    assert output == 5
