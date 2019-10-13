import numbers


def my_sum(a, b):
    """
    Sums two variables and returns the result.
    Both parameters should be numbers.
    :param a: first addend
    :param b: second addend
    :return: sum of the addends
    """
    assert (is_number(a) and is_number(b)), 'Both addends should be numbers'
    return a + b


def is_number(x):
    """
    Check whether the object provided is a number.
    :param x: object to check
    :return: True if x is a number
    """
    return isinstance(x, numbers.Number)
