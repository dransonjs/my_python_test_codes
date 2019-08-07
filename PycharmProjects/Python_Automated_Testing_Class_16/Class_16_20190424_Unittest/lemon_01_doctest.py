# 使用python内置的doctest测试


def mul(a, b):
    """
    >>> mul(10, 2)
    20
    >>> mul('y', 2)
    'yy'
    """
    return a * b


def add(a, b):
    """
    >>> add(-2, -1)
    -3
    >>> add(0, 0)
    1
    """
    return a + b


