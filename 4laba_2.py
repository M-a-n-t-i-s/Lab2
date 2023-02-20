import sqlalchemy
import pandas as pd
import pymorphy2
import re

db = sqlalchemy.create_engine('sqlite:///books_db.sqlite')
df = pd.read_sql_query('select chunk_id, author, text from chunk',
                       db, index_col='chunk_id')
df.head(10)
print("Начало процесса...")
morph = pymorphy2.MorphAnalyzer()


def is_cyr_word(word):
    for ch in word:
        if not ('а' <= ch <= 'я'):
            return False
    return True


def process_text(text):
    lower = (word.lower() for word in re.split(r'\W+', text))
    cyr = (word for word in lower if len(word) > 0 and is_cyr_word(word))
    norm_form = (morph.parse(word)[0].normal_form for word in cyr)

    return ' '.join(norm_form)


df['text'] = df['text'].map(process_text)
for text in df['text']:
    words = text.split()
print(words)
print("Конец")

dict1 = dict()
set1 = set()
for i in df['text']:
    w = i.split()
    set1.clear()
    for el in w:
        if el not in set1:
            set1.add(el)
            if el not in dict1:
                dict1[el] = 1
            else:
                dict1[el] = dict1.get(el) + 1
ans = dict(sorted(dict1.items(), key=lambda t: t[1], reverse=True))

items = list(ans.items())
print(items[:20])

top200 = [y for y in ans][:200]

dict2 = dict()
set2 = set()
for i in range(1, len(df['text'])):
    if (df['author'][i] == 'Андрей Платонович Платонов'):
        w = df['text'][i].split()
        set2.clear()
        for el in w:
            if el not in top200:
                if el not in set2:
                    set2.add(el)
                    if el not in dict2:
                        dict2[el] = 1
                    else:
                        dict2[el] = dict2.get(el) + 1

answer = dict(sorted(dict2.items(), key=lambda t: t[1], reverse=True))
count = 0
items = list(answer.items())
print(items[:20])
