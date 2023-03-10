# -* coding: utf-8 *-
# Файл для создания сводных таблиц со всеми уникальными значениями из базы данных
import pandas as pd


# Подключаемся к главной БД
db = pd.read_csv("test.csv", sep='|', dtype={'pages': 'str'})
# Создаем переменный для хранения столбцов будущей сводной таблицы
publishings = set()
book_types = set()
bbks = set()
udks = set()
disciplines = set()
authors = set()
isbns = set()

# Производим необходимые преобразования (проходимся по всем значениям столбца и добавляем во множество)
for bbk in db['bbk']:
    bbk_parts = bbk.split('/')
    [bbks.add(i) for i in bbk_parts]
for udk in db['ydk']:
    udk_parts = udk.split('/')
    [udks.add(i) for i in udk_parts]
for discipline in db['discipline']:
    discipline_parts = discipline.split(',')
    [disciplines.add(i) for i in discipline_parts]
for author in db['author']:
    author_part = str(author).split(',')
    [authors.add(i.strip()) for i in author_part]
for isbn in db['isbn']:
    isbns.add(isbn)

# Записываем уникальные значения в переменные, сортируя в порядке возрастания
publishings = sorted([str(i) for i in list(set(db['publishing'])) if str(i) not in ['', 'nan']])
book_types = sorted([str(i) for i in list(set(db['book_type'])) if str(i) not in ['', 'nan']])
bbks = sorted(bbks)
udks = sorted(udks)
disciplines = sorted(disciplines)
authors = sorted(authors)
isbns = list(isbns)

# Количество строк в столбцах должно быть равным, поэтому добавим пустые строки, если их не хватает
rows_count = max(len(publishings), len(book_types), len(bbks), len(udks), len(disciplines), len(authors), len(isbns))
[publishings.append('nan') for _ in range(rows_count - len(publishings))]
[book_types.append('nan') for _ in range(rows_count - len(book_types))]
[bbks.append('nan') for _ in range(rows_count - len(bbks))]
[udks.append('nan') for _ in range(rows_count - len(udks))]
[disciplines.append('nan') for _ in range(rows_count - len(disciplines))]
[authors.append('nan') for i in range(rows_count - len(authors))]
[isbns.append('ana') for i in range(rows_count - len(isbns))]

# Создаем общий массив данных и записываем сводную таблицу в csv файл
data = [[publishings[i], book_types[i], bbks[i], udks[i],
         disciplines[i], authors[i], isbns[i]] for i in range(rows_count)]
new_db = pd.DataFrame(data, columns=['publishing', 'book_type', 'bbk', 'udk', 'discipline', 'author', 'isbn'])
new_db.to_csv('summary_table.csv', sep='|', index=False)
