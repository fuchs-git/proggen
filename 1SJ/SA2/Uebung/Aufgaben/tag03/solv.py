import re

with open("datadump.txt", "r") as f:
    data = f.read()


pattern = r"mul\([0-9]{1,3},[0-9]{1,3}\)"
x = re.findall(pattern, data)

sum = 0
for term in x:
    a= int(term.split("(")[1].split(",")[0])
    b= int(term.split("(")[1].split(",")[1].replace(")",""))
    sum += a*b

print(sum)