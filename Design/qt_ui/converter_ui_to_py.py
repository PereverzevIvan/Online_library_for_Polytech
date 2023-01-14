# -* coding: utf-8 *-
import os
import re


def generate_all_ui2py(path: str):
    files = os.listdir(path)
    ui_list = []
    pattern = re.compile(r'.*\.ui')
    for it in files:
        if pattern.match(it):
            ui_list.append(it)

    for it in ui_list:
        file_path = os.path.join(path, it)
        file_name = file_path.split(os.sep)[-1]
        file_name_without_extension = file_path.split(os.sep)[-1].removesuffix('.ui')
        cmd = f"pyside6-uic 'E:/Projects on Python/Online_library_for_Polytech/Design/qt_ui/{file_name}' " \
              f"> 'E:/Projects on Python/Online_library_for_Polytech/Design/qt_ui/ui_{file_name_without_extension}.py'"
        print(cmd)


if __name__ == '__main__':
    generate_all_ui2py(os.path.dirname((os.path.abspath(__file__))))
