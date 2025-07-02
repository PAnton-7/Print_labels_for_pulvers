from time import sleep
import logging

import pandas as pd
import ctypes
from lexicon import LEXICON
from df_processing import task_rw_df_to_lable_df
from lable_img_code import lable_like_excel_code


PRINTER_PORT = "TSC TE200"

logger = logging.getLogger()
log_file = '\\\\diskstation\\exchange-inspector\\Для офиса\\Temp\\Labels_log.log'
# log_rec_format = '%(filename)s:%(lineno)d #%(levelname)-8s[%(asctime)s] - %(name)s - %(message)s'
log_rec_format = '[%(asctime)s] %(levelname)-8s - %(name)s - %(message)s - %(filename)s:%(lineno)d'

logging.basicConfig(filename=log_file, encoding='utf-8', level=logging.INFO, format=log_rec_format)
# logger.info('Запущена печать бирок')

def on_printer_lib(path: str = ".//TSCLIB.dll"):
    return ctypes.WinDLL(path)


def set_up_printer(tsclibrary):
    # Открывам порт принтера
    tsclibrary.openportW(PRINTER_PORT)
    # Задаем конфигурацию бирки
    tsclibrary.sendcommandW("SIZE 58 mm, 40 mm")
    tsclibrary.sendcommandW("GAP 2 mm, 0 mm")
    # Задаем направление печати
    tsclibrary.sendcommandW("DIRECTION 1")
    # Очищаем буфер изображений
    tsclibrary.sendcommandW("CLS")
    tsclibrary.closeport()


def print_labels(tsclibrary) -> None:
    tsclibrary.openportW(PRINTER_PORT)
    pd.set_option('display.max_columns', None)
    # Получаем DF с данными всех этикетов
    labels_df = task_rw_df_to_lable_df()
    labels_df.reset_index(drop=True, inplace=True)

    # Разбиваем датафрейм со всеми бирками на строки (отдельные бирки)
    for one_label in labels_df.iterrows():
        # Переводим объект Series в словарь
        one_label_dict = one_label[1].to_dict()

        # Cоздаем образ этикетки
        try:
            lable_like_excel_code(tsclibrary, one_label_dict)

            # Формируем текст QR-кода, и добавляем его на бирку
            qrcode = f'{one_label[1][LEXICON["Reference"]]}R{one_label[1][LEXICON["Lot #"]]}'
            tsclibrary.sendcommandW(f'QRCODE 330, 144, H, 5, A, 0, J1, M2, "{qrcode}"')
            # Печатаем бирку
            tsclibrary.sendcommandW("PRINT 1, 1")
            # Очищаем буфер принтера для новой этикетки
            tsclibrary.sendcommandW("CLS")
        except Exception as e:
            print(f'Произошла ошибка: {str(e)}')
            sleep(5)
            tsclibrary.sendcommandW("CLS")

    tsclibrary.closeport()


def main():
    printer_lib = on_printer_lib(".//TSCLIB.dll")
    set_up_printer(printer_lib)
    print_labels(printer_lib)


if __name__ == '__main__':
    main()
