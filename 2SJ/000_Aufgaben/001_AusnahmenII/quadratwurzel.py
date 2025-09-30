import math

def wurzel(x):
    assert isinstance(x, (int, float)), f"Eingabewert x muss ein int oder float sein, aber ist <class 'str'>"
    try:
        return math.sqrt(x)
    except ValueError:
        return(f'ValueError: Negative Zahl {x} kann nicht verwurzelt werden')

print(wurzel(-4))
