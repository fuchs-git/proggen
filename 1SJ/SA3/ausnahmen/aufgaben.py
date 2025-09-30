from typing import Any


def devision_mit_rest(dividend: Any=1, divisor: Any=0) -> tuple:
    try:
        int(dividend); int(divisor)
        return divmod(dividend, divisor)
    except ZeroDivisionError:
        return (dividend, divisor)
    except ValueError:
        return 1,0


print(devision_mit_rest(13, 4.1))
print(devision_mit_rest())
