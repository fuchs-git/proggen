import re
from itertools import count

with open('NEWSTICKER.html', encoding='utf8') as f:
    data = f.read()

print(len(data))


artikel = set()
pattern1 = r'<article class="ticker__item" data-id="([a-z]{0,1}[0-9]{8})">'
treffer = re.findall(pattern1, data, re.DOTALL)
[artikel.add(x) for x in treffer]
print(len(artikel))

pattern2 = pattern1 + (r'.*?<time class="ticker__time" datetime="(.*?)">(?:.*?)</time>.*?'
                       r'<span class="ticker__title">([^<]*?)</span>')
treffer = re.findall(pattern2, data, re.DOTALL)
print(len(treffer))

pattern3 = pattern1 + r'.*?<span class="ticker__tag">(Sicherheit|sicherheit)</span>.*?'
treffer = re.findall(pattern3, data, re.DOTALL)
print(len(treffer))
