# -------------------------------------------------------------------------------------------------------------
# 1. 2D-Druck
# Wenn Sie eine zweidimensionale Liste mit print ausgeben lassen, wird die Liste in einer Zeile dargestellt.
# Das könnte für zweidimensionale Listen unbefriedigend sein.
#
# Erstellen Sie eine Funktion print_2d, welche eine zweidimensionale Liste so ausgibt,
# dass die Elemente der ersten Dimension jeweils auf einer neuen Zeile stehen.
# -------------------------------------------------------------------------------------------------------------

liste = [['A1', 'A2', 'A3', 'A4'], ['B1', 'B2', 'B3', 'B4'], ['C1', 'C2', 'C3', 'C4']]
print(*[x for x in liste], sep='\n')

for i in liste: print(i)