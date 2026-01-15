import re

regex = r"(a)(b)c"
string = "asdsadasabcbcasdabcbabf"
treffer = re.findall(regex, string, re.DOTALL)
print(treffer)

# ohne findall
regex = r"(a)(b)c"
string = "asdsadasabcbcasdabcbabfabc"
treffer = re.finditer(regex, string)
print(*[f'{x.groups()} auf Position {x.start()}' for x in treffer], sep='\n')


pattern = r'(x+)(x+)(y)'
string = "xxxxxxxxxxxxxxxxxxxxxxy"
treffer = re.findall(pattern, string)
print(treffer)


pattern = r'([^,]*),'
string = "asdf,asdf,asdf,asdf,asdf,asdf,asdf,asdf,asdf,asdf,asdf"
treffer = re.findall(pattern, string)
print(treffer)