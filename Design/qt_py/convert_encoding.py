# -* coding: utf-8 *-
import os
import re


def convert_encoding(path: str):
    files = os.listdir(path)
    ui_list = []
    for it in files:
        if 'ui' in it:
            ui_list.append(it)

    for it in ui_list:
        file_path = os.path.join(path, it)
        try:
            file = open(file_path, mode='r', encoding='utf-16le')
            data = file.readlines()
        except UnicodeDecodeError:
            file = open(file_path, mode='r', encoding='utf-8')
            data = file.readlines()
        file.close()
        file = open(file_path, mode='w', encoding='utf-8')
        file.writelines(data)


if __name__ == '__main__':
    convert_encoding(os.path.dirname((os.path.abspath(__file__))))
