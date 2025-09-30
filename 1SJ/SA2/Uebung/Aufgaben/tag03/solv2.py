import re

with open("datadump.txt", "r") as f:
    data = f.read()

m_pattern = r"mul\([0-9]{1,3},[0-9]{1,3}\)"
pattern = r"(do\(\)|don't\(\))"

check = True
summe = 0
test = re.split(pattern, data)

for elem in test:
    if elem == "do()":
        check = True
    elif elem == "don't()":
        check = False
    if check:
        y = re.findall(m_pattern, elem)
        for x in y:
            a = int(x.split("(")[1].split(",")[0])
            b = int(x.split("(")[1].split(",")[1].replace(")", ""))
            summe += a * b

print(summe)
