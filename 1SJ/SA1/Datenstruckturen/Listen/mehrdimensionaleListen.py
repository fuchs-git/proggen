brett = []
for i in "ABCDEFGH":
    neue_zeile = []
    for j in "12345678":
        neue_zeile.append(i+j)
    brett.append(neue_zeile)

# print(*brett, sep='\n')


# def e_count(text):
#     eee = 0
#     for char in text:
#         if char == "e":
#             eee += 1
#     return eee

def e_count(text):
    return len([x for x in text.lower() if x == "e"])


print(e_count("Beispielwörter = Erdbeere, Eichhörnchen, Eisenbahnschienenleitsystemüberwachungsstationbearbeiterinnen"))

def count(text):
    return text.lower().count("e")

print(count("Beispielwörter = Erdbeere, Eichhörnchen, Eisenbahnschienenleitsystemüberwachungsstationbearbeiterinnen"))
