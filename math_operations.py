def sum_xy(x, y):
    return x + y


def div_xy(x, y):
    return x / y


def sub_xy(x, y):
    return x - y


def multy_xy(x, y):
    return x * y


def power_xy(x, y):
    return x ** y


def abs_x(x):
    if x >= 0:
        return x
    else:
        return -x


def sqrt_x(num, e=1e-5):
    result = num / 2
    while True:
        root = 0.5 * (result + num / result)
        if abs_x(root - result) < e:
            return result
        result = root


