import time
import pandas as pd
from random import randint


def sheet_check(sheet_name=None):

    while sheet_name != '' and sheet_name not in pd.ExcelFile(f'{file_name}.xlsx').sheet_names:
        sheet_name = input(f'виберіть зі списку лист для опитування\n'
                           f'(за замовчуванням буде вибрано перший)\n'
                           f'{pd.ExcelFile(f"{file_name}.xlsx").sheet_names}: ')
    return sheet_name


def cleaner(file_name, sheet_name=''):

    data = pd.read_excel(f'{file_name}.xlsx') if sheet_name == '' else pd.read_excel(f'{file_name}.xlsx', sheet_name)
    words = data.values.tolist()
    words = [item for item in words if not pd.isna(item[1])]
    return words


def quiz(words_list):

    answer = None
    right, wrong = 0, 0

    while answer != 'stop':
        w_num = randint(0, len(words_list) - 1)
        answer = input(f'{words_list[w_num][1]} \n')
        if answer.lower() in [i.lower() for i in words_list[w_num]]:
            right += 1
        elif answer == 'stop':
            continue
        else:
            wrong += 1
            print(f'правильно буде {words_list[w_num][0]}')

    print(f'right: {right}, wrong: {wrong}')
    time.sleep(10)


print('для використання стандартних значень просто нажимайте ентер')
time.sleep(4)

print('я лінива собака, тому відповідальність за адекватну\n'
      'назву файлів і листів у файлах лежить\n'
      'цілком і повністю на тому,\n'
      'хто буде використовувати цю фігню')
time.sleep(6)

name = input('введіть назву файлу: ')
file_name = 'dictionary' if name == '' else name

sheet_name = sheet_check()
words = cleaner(file_name, sheet_name)
quiz(words)
