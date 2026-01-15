import re

regex = r"Erdbeeren|Bananen|Birnen"
string = "Ich mag Erdbeeren. Bananen sind toll. Es sollte mehr Birnen geben!"

print(re.sub(regex, "Früchte", string))