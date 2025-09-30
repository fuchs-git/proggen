def summe_der_quadrate(lst: list):
    for x in lst:
        assert isinstance(x, (int, float)), f"Liste enthält ungültige Elemente: {x}"
    return sum([x**2 for x in lst])

a = [1, 2, 3]
print(summe_der_quadrate(a))
