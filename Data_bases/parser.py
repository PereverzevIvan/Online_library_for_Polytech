import os.path

from bs4 import BeautifulSoup as bs
from bs4 import Comment
import requests
import pandas as pd
import time
import os


def correct_str(s):
    res = ""
    sz = len(s)
    if sz == 0:
        return res
    i = 0
    while s[i] == ' ' or s[i] == '\n':
        i += 1
        if i == sz:
            i -= 1
            break
    l = i
    i = len(s) - 1
    while s[i] == ' ' or s[i] == '\n':
        i -= 1
        if i == -1:
            i += 1
            break
    r = i
    res += s[l]
    for i in range(l + 1, r + 1):
        if s[i] == ' ' or s[i] == '\n':
            if s[i - 1] == ' ' or s[i - 1] == '\n':
                continue
        res += s[i]
    if res == '\n' or res == ' ':
        res = ""
    return res


def parse_all_znanium():
    BASIC_URL = "https://znanium.com"
    URL_PREF = "https://znanium.com/catalog/wide-search?submitted=1&insubscribe=0&per-page=100&theme%5B%5D=9aed8e64-f212-11e8-8985-90b11c31de4c&location=-1&page="
    URL_SUF = ""
    FILEOUT_NAME = "znanium_preparse.csv"

    if not os.path.exists("../Design/images"):
        os.makedirs("../Design/images")

    r = requests.get(URL_PREF + str(1) + URL_SUF)
    soup = bs(r.text, "html.parser")

    paging = soup.find_all('div', class_="paging__item")
    last_page = int(paging[-1].text)
    print("Количество страниц: ", last_page)

    result_list = {'link': [], "isbn": [], 'annotation': [], "bbk": [], 'ydk': [],
                   "bibl_record": []}

    isbn_dict = {}

    df = pd.DataFrame(data=result_list)
    df.to_csv(FILEOUT_NAME, index=False)

    for page in range(1, last_page + 1):
        r = requests.get(URL_PREF + str(page))
        soup = bs(r.text, "html.parser")
        books_list = soup.find_all('div', class_="book-list__item")

        result_list = {'link': [], "isbn": [], 'annotation': [], "bbk": [], 'ydk': [],
                       "bibl_record": []
                       }

        for book in books_list:
            book_header = book.find(class_="book-list__title")
            book_link = BASIC_URL + book_header.parent.get("href")
            r = requests.get(book_link)
            # r=requests.get("https://znanium.com/catalog/document?id=422978")
            soup = bs(r.text, "html.parser")
            used_result = {'isbn': False, "ydk": False, "bbk": False, 'annotation': False, 'bibl_record': False}
            for comment in soup.find(class_="book-hidden-more").find_all(text=lambda text: isinstance(text, Comment)):
                if correct_str(comment) == "ISBN":
                    x = correct_str(comment.next_sibling.next_sibling.text)

                    if len(x) > 4:

                        if x[:4] == 'ISBN':
                            l = 6
                            if x[l] == ' ' or x[l] == '\n':
                                l += 1
                            r = len(x)
                            book_isbn = x[l:r]
                            used_result['isbn'] = True
                            break
            if not used_result['isbn']:
                print("Not found ISBN")
                print(book_link)
                continue

            book_img = soup.find(class_="book-single__img-wrap").find('img')
            book_cover = BASIC_URL + book_img.get('src')

            book_info = soup.find(class_="_book-tabs")

            book_annotation = book_info.find('div', {"nav": "ant"})

            if book_annotation != None:
                book_annotation = correct_str(book_annotation.text)
                used_result['annotation'] = True

            book_bibl_record = book_info.find('pan', {"id": "doc-biblio-card"})

            if book_bibl_record != None:
                book_bibl_record = correct_str(book_bibl_record.text)
                used_result["bibl_record"] = True

            book_class = book_info.find('div', {"nav": "classfy"})

            for line in book_class:
                if correct_str(line.text) == "УДК:":
                    book_ydk_text = correct_str(line.next_sibling.next_sibling.text)
                    book_ydk = []
                    l = 0
                    i = 0
                    while i < len(book_ydk_text):

                        if book_ydk_text[i] == ':':
                            m = i
                            i += 2
                            while book_ydk_text[i] != '\n':
                                i += 1
                                if i == len(book_ydk_text):
                                    break
                            book_ydk.append([book_ydk_text[l:m], book_ydk_text[m + 2:i]])
                            l = i + 1
                        i += 1
                    used_result['ydk'] = True
                    continue
                if correct_str(line.text) == "ББК:":
                    book_bbk_text = correct_str(line.next_sibling.next_sibling.text)

                    book_bbk = []
                    l = 0
                    i = 0
                    while i < len(book_bbk_text):

                        if book_bbk_text[i] == ':':
                            m = i
                            i += 2
                            while book_bbk_text[i] != '\n':
                                i += 1
                                if i == len(book_bbk_text):
                                    break
                            book_bbk.append([book_bbk_text[l:m], book_bbk_text[m + 2:i]])
                            l = i + 1
                        i += 1
                    used_result['bbk'] = True
                    continue

            flag_add = True
            for key in used_result:

                if not used_result[key]:
                    print(key, 'Not Found')
                    flag_add = False

            if flag_add:
                if book_isbn in isbn_dict:
                    print("ISBN_Key already exist")
                    print(book_link)
                    continue
                isbn_dict[book_isbn] = 1
                result_list['link'].append(book_link)
                result_list["isbn"].append(book_isbn)
                result_list['annotation'].append(book_annotation)
                result_list["bbk"].append(book_bbk)
                result_list['ydk'].append(book_ydk)
                result_list["bibl_record"].append(book_bibl_record)
                # Скачивание изображения обложки книги

                with open("../Design/images/" + str(book_isbn) + '.jpg', 'wb') as handle:
                    response = requests.get(book_cover, stream=True)

                    for block in response.iter_content(1024):
                        if not block:
                            break
                        handle.write(block)
            else:
                print(book_link)
        os.system('cls')
        print("{0:0.2f}".format(page / last_page * 100), '%', sep='')
        df = pd.DataFrame(data=result_list)
        df.to_csv(FILEOUT_NAME, mode='a', index=False, header=False)
    print('Done')


def parse_csv_search_znanium():
    FILEOUT_NAME = "data_base.csv"
    BASIC_URL = "https://znanium.com"

    if not os.path.isfile("znanium_preparse.csv"):
        print("Preparse wasn't complited")
        return

    preload_mas = pd.read_csv("znanium_preparse.csv").to_numpy()

    link_dict = {}
    for i in range(len(preload_mas)):
        link_dict[str(preload_mas[i][0])] = [-1, i]

    fi = pd.read_csv("дисциплины.csv").to_numpy()
    tag_dict = {}
    for row in fi:
        tags = []
        i = 0
        while i < len(row[1]):
            tag = ""
            if row[1][i] == ' ':
                i += 1
                continue
            while row[1][i] != ',':
                tag += row[1][i]
                i += 1
                if i == len(row[1]):
                    break
            tags.append(tag)
            if not tag in tag_dict:
                tag_dict[tag] = []
            tag_dict[tag].append(row[0])
            i += 1

    final_mas = {
        "title": [], "publishing": [], "year": [],
        "pages": [], "book_type": [], "lvl_education": [], "author": [], "discipline": [],
        "isbn": [], "bbk": [], "ydk": [], "bibl_record": [], "annotation": [], "link": []
    }

    cnt = 1
    cnt_n = len(tag_dict)

    for search_text in tag_dict:
        URL = "https://znanium.com/catalog/wide-search?submitted=1&insubscribe=0&per-page=100&sub=1&" + \
              "title=" + search_text + \
              "&theme%5B%5D=9aed8e64-f212-11e8-8985-90b11c31de4c&location=-1&page="
        r = requests.get(URL + '1')
        soup = bs(r.text, "html.parser")
        paging = soup.find_all('div', class_="paging__item")
        if len(paging):
            last_page = int(paging[-1].text)
        else:
            last_page = 1
        n = last_page

        result_list = {'link': [], 'title': [], 'publishing': [],
                       'year': [], 'pages': [], 'book_type': [], 'lvl_education': [],
                       'author': [],
                       }

        for page in range(1, n + 1):
            result = {'link': [], 'title': [], 'publishing': [],
                      'year': [], 'pages': [], 'book_type': [], 'lvl_education': [],
                      'author': []
                      }
            r = requests.get(URL + str(page))
            soup = bs(r.text, 'html.parser')

            books_list = soup.find_all('div', class_="book-list__item")

            for book in books_list:

                book_header = book.find(class_="book-list__title")
                book_link = BASIC_URL + book_header.parent.get("href")
                # print(book_link)

                if not book_link in link_dict:
                    # print("not found by link")
                    # print(book_link)
                    continue

                result['link'].append(book_link)
                result['title'].append(correct_str(book_header.text))

                # book_img = book.find(class_="book-list__img").find('img')

                book_properties = book.find(class_="book-list__chars").find_all(class_="book-list__char")
                used_properties = {'publishing': False,
                                   'year': False, 'pages': False, 'book_type': False, 'lvl_education': False,
                                   'author': False}

                for property in book_properties:
                    property_text = correct_str(property.text)
                    if len(property_text) == 0:
                        continue

                    if len(property_text) >= len('Авторы:'):
                        if property_text[:len('Авторы:')] == 'Авторы:':
                            l = len('Авторы:')
                            r = len(property_text)

                            if property_text[l] == ' ' or property_text[l] == '\n':
                                l += 1
                            result['author'].append(property_text[l:r])
                            used_properties['author'] = True
                            continue
                    if len(property_text) >= len('Издательство:'):
                        if property_text[:len('Издательство:')] == 'Издательство:':
                            l = len('Издательство:')
                            r = len(property_text)

                            if property_text[l] == ' ' or property_text[l] == '\n':
                                l += 1
                            result['publishing'].append(property_text[l:r])
                            used_properties['publishing'] = True
                            continue
                        # if len(property_text) >= len('Вид издания:'):
                        if property_text[:len('Вид издания:')] == 'Вид издания:':
                            l = len('Вид издания:')
                            r = len(property_text)

                            if property_text[l] == ' ' or property_text[l] == '\n':
                                l += 1
                            result['book_type'].append(property_text[l:r])
                            used_properties['book_type'] = True
                            continue
                        # if len(property_text) >= len('Уровень образования:'):
                        if property_text[:len('Уровень образования:')] == 'Уровень образования:':
                            l = len('Уровень образования:')
                            r = len(property_text)

                            if property_text[l] == ' ' or property_text[l] == '\n':
                                l += 1
                            result['lvl_education'].append(property_text[l:r])
                            used_properties['lvl_education'] = True
                            continue
                    if len(property_text) >= len('Год издания:'):
                        if property_text[:len('Год издания:')] == 'Год издания:':
                            l = len('Год издания:')
                            if property_text[l] == ' ' or property_text[l] == '\n':
                                l += 1

                            for sim in range(len(property_text)):
                                if property_text[sim] == "К":
                                    break

                            if property_text[sim] == "К":
                                if property_text[sim - 1] == ' ' or property_text[sim - 1] == '\n':
                                    r = sim - 1
                                else:
                                    r = sim
                            else:
                                r = sim + 1

                            result['year'].append(property_text[l:r])
                            used_properties['year'] = True

                            if property_text[sim] == "К":
                                sim += len("Кол-во страниц:")
                                l = sim + 1
                                if property_text[l] == ' ' or property_text[l] == '\n':
                                    l += 1
                                r = len(property_text)
                                result['pages'].append(property_text[l:r])
                                used_properties['pages'] = True

                for key in used_properties:
                    if not used_properties[key]:
                        result[key].append("")
            for key in result:
                for item in result[key]:
                    result_list[key].append(item)

            for i in range(len(result_list['link'])):
                if link_dict[result_list['link'][i]][0] == -1:
                    link_dict[result_list['link'][i]][0] = len(final_mas['link'])
                    idx = link_dict[result_list['link'][i]][0]
                    idx2 = link_dict[result_list['link'][i]][1]
                    for key in result_list:
                        final_mas[key].append(result_list[key][i])

                    final_mas["isbn"].append(preload_mas[idx2][1])
                    final_mas["annotation"].append(preload_mas[idx2][2])
                    final_mas["bbk"].append(preload_mas[idx2][3])
                    final_mas["ydk"].append(preload_mas[idx2][4])
                    final_mas["bibl_record"].append(preload_mas[idx2][5])
                    final_mas['discipline'].append({})
                    for j in tag_dict[search_text]:
                        final_mas['discipline'][idx][j] = True
                else:
                    idx = link_dict[result_list['link'][i]][0]
                    for j in tag_dict[search_text]:
                        final_mas['discipline'][idx][j] = True

            print(search_text, " - {0:0.2f}".format(page / n * 100), '%', sep='')
        os.system('cls')
        print("{0:0.2f}".format(cnt / cnt_n * 100), '%', sep='')
        cnt += 1

    for i in range(len(final_mas['discipline'])):
        x = final_mas['discipline'][i]
        y = ""
        for j in x:
            y += j + ','
        y = y[:-1]
        final_mas['discipline'][i] = y

    print('Making Dataframe')
    df = pd.DataFrame(data=final_mas)
    print('Writing to csv')
    df.to_csv(FILEOUT_NAME, index=False)
    print('Done')

    print("Editing csv for library")
    editcsv(FILEOUT_NAME)
    print('Done')

#  Приводит формат csv для чтения библиотекой


def editcsv(fi_name):
    fi = pd.read_csv(fi_name, dtype={'pages': 'str'})

    for cur_row in range(len(fi['ydk'])):
        i_ydk = 0
        ydk = []

        while i_ydk < len(fi['ydk'][cur_row]):
            val1 = ""
            val2 = ""
            if (fi['ydk'][cur_row][i_ydk] == '['):
                i_ydk += 2
                while (fi['ydk'][cur_row][i_ydk + 1] != ','):
                    val1 += fi['ydk'][cur_row][i_ydk]
                    i_ydk += 1
                i_ydk += 4
                while (fi['ydk'][cur_row][i_ydk] != "'"):
                    val2 += fi['ydk'][cur_row][i_ydk]
                    i_ydk += 1
                ydk.append([val1, val2])
            i_ydk += 1
        fi['ydk'][cur_row] = ""
        for val in ydk:
            fi['ydk'][cur_row] += val[0] + ',' + val[1] + '/'
        fi['ydk'][cur_row] = fi['ydk'][cur_row][:-1]

    for cur_row in range(len(fi['bbk'])):
        i_bbk = 0
        bbk = []
        while i_bbk < len(fi['bbk'][cur_row]):
            val1 = ""
            val2 = ""
            if (fi['bbk'][cur_row][i_bbk] == '['):
                i_bbk += 2
                while (fi['bbk'][cur_row][i_bbk + 1] != ','):
                    val1 += fi['bbk'][cur_row][i_bbk]
                    i_bbk += 1
                i_bbk += 4
                flag = 0
                while (fi['bbk'][cur_row][i_bbk] != "'"):
                    val2 += fi['bbk'][cur_row][i_bbk]
                    i_bbk += 1
                bbk.append([val1, val2])
            i_bbk += 1
        fi['bbk'][cur_row] = ""
        for val in bbk:
            fi['bbk'][cur_row] += val[0] + ',' + val[1] + '/'
        fi['bbk'][cur_row] = fi['bbk'][cur_row][:-1]

    fi.to_csv('test.csv', index=False, sep='|')


def run():
    while True:
        req_type = input("Введите: \n"
                         "1. Препарсинг всех книг\n"
                         "2. Создания конечной БД используя таблицу дисциплин и их тегов для поиска\n"
                         "Примечание: Необходим препарсинг всех книг\n"
                         "3. Выход из программы\n")
        req_type = correct_str(req_type)

        if req_type == "1":
            start_time = time.time()
            print("Starting")
            parse_all_znanium()

            end_time = time.time()
            interval_time = end_time - start_time
            print("{0:.1f} seconds\n{1:.1f} minutes\n{2:.1f} hours".format(interval_time, interval_time / 60,
                                                                           interval_time / 3600))

        elif req_type == "2":
            start_time = time.time()
            print("Starting")
            parse_csv_search_znanium()

            end_time = time.time()
            interval_time = end_time - start_time
            print("{0:.1f} seconds\n{1:.1f} minutes\n{2:.1f} hours".format(interval_time, interval_time / 60,
                                                                           interval_time / 3600))
        elif req_type == "3":
            return
        else:
            print("Incorrect input. Try again")


run()
