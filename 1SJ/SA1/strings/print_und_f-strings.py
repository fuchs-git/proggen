x = 179
print(f"{x}, {x:b}, {x:#b}")
print(f"{x}, {x:o}, {x:#o}")
print(f"{x}, {x:d}, {x:#d}")
print(f"{x}, {x:n}, {x:#n}")
print(f"{x}, {x:x}, {x:#x}")
print(f"{x}, {x:X}, {x:#X}")


print(f'{5:<25}') # linksbündig
print(f'{3+4:>25}') # rechtsbündig
print(f'{17/3:^25}') # mittig
print(f'{"Bob":<25}') # links
print(f'{"Alice":->25}') # rechts mit -
print(f'{" Alice + Bob ":x^25}') # mittig mit x

x = 123
print(f"{x:.2f}")

print(f'ein f-String mit {{geschweiften Klammern}} und einem Ausdruck {3+5=}')

for zahl in range(5):
    print(f'Formatierung von Dingen {zahl:0{zahl + 1}} VARIABEL {zahl:{5 - zahl}} machen ')

h = 'HeuhaufenHeuhaufenHeuhaufenHeuhaufenNadelHeuhaufenHeuhaufenHeuhaufen'
n = 'Nadel'
print(x,x,x,x, sep="€€€€€")


