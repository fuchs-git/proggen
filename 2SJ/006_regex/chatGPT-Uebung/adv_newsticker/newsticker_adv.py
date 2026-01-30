import re

with open('ADV_NEWSTICKER.html', "r", encoding='utf8') as f:
    data = f.read()

print(len(data))


# Aufgabe 1
pattern1 = r'<article[^>]*>'
treffer = re.findall(pattern1, data, re.DOTALL)
print(len(treffer))


# Aufgabe 2 
# <article class="ticker__item" data-id="n91000000">
pattern2 = (r'<article class="ticker__item" data-id="(?P<ID>[n][\d]{8})">\s*'
            r'<time class="ticker__time" datetime="(?P<Date>[^"]*)">[^<]*</time>')


treffer = re.finditer(pattern2, data, re.DOTALL)
[print(f'{x.group('ID')} {x.group('Date')}') for x in treffer]
