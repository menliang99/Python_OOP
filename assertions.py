def divider_secure(number, divisor):
    if divisor == 0:
        raise ValueError("The divisor is 0!")
    return number / divisor


def divider_secure_assert(number, divisor):
    assert divisor != 0, "Divided a number by zero!"
    return number / divisor


print (divider_secure_assert(10, 0))
