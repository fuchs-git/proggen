import mathe_operationen as mo
import math as m

print(f'{mo.addieren(5,3)=}')
print(f'{mo.subtrahieren(5,3)=}')
print(f'{mo.multiplizieren(5,3)=}')
print(f'{mo.dividieren(5,3)=}')

obj = mo.Strichrechnung(5,7)
print(f'{obj.subtrahieren()=}')
print(f'{obj.addieren()=}')


pi = 9
print(pi)
print(m.pi)
