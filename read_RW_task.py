import logging
from typing import Tuple
import pandas as pd
from pandas import DataFrame
from tkinter import filedialog
# from openpyxl.worksheet.filters import CustomFilterValueDescriptor

logger = logging.getLogger()

def monkey_set(self, instance, value):
    pass


# CustomFilterValueDescriptor.__set__ = monkey_set


def read_rw_task(path: str = None) -> Tuple[DataFrame, str]:
    # Настраиваем текущую версия для операции df.fillna(value=0, inplace=True)
    pd.set_option('future.no_silent_downcasting', True)
    # читаем файл
    task_df: DataFrame = pd.read_excel(io=path, skiprows=1, usecols=lambda x: 'Unnamed' not in x)
    task_df.info()
    task_df = task_df[(task_df['ЛОТ №'].notnull()) & (task_df['ЛОТ №'] != '*')]

    print()
    print(f'Найдено задание:\n{path}\nна {task_df.shape[0]} лотов')
    logger.info(path)

    return task_df, path


def choose_file() -> str:
    filename = filedialog.askopenfilename(initialdir='\\\\DISKSTATION\\exchange-inspector\\01 ЗАДАНИЯ НА СМЕНУ', title='Выбери файл с заданием')
    print(f'выбран файл {filename}')
    return filename


def get_df() -> Tuple[DataFrame, str]:
    df, path = read_rw_task(choose_file())

    # Судовой пример
    # path: str = '\\\\DISKSTATION\\exchange-inspector\\01 ЗАДАНИЯ НА СМЕНУ\\2023\\06 JUNE\\ЗАДАНИЕ ПО СУДАМ\\Судовые бирки\\судовые на 23.06.2023.xlsm'
    # df = read_rw_task(path)

    # Вагонный пример
    # path: str = '\\\\DISKSTATION\\exchange-inspector\\01 ЗАДАНИЯ НА СМЕНУ\\2023\\06 JUNE\\ЗАДАНИЕ ПО ВАГОНАМ\\задание на 23.06.2023.xlsx'
    # df = read_rw_task(path)
    return df, path


def main():
    print(get_df())


if __name__ == '__main__':
    main()
