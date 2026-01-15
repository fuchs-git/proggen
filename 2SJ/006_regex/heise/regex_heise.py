import re

suche = '''
      <h3
        class="
          a-article-teaser__title

        "
      >

        <span class="a-article-teaser__title-text">„Anthem“ vor der Abschaltung: Online-Shooter geht in sein letztes Wochenende
        </span>
      </h3>
'''

pattern2 = r'<span[^>]*class="a-article-teaser__title-text"[^>]*>(.*?)</span>'


pattern = r'<h3[^>]\s*.*?Shooter.*?</h3>'
with open('newsticker.txt', encoding='utf8') as f:
    file = f.read()

print(re.findall(pattern2, file, re.DOTALL))

