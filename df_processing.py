import pandas as pd
from typing import Tuple
from pandas import DataFrame
from read_RW_task import get_df
from lexicon import LEXICON, analytycal_sample_header
from datetime import datetime
from math import modf
from transliterate import translit

def isfloat(num):
    try:
        int(num)
        return True
    except:
        return False


def check_weight(num: float | str | int) -> str:
    """Если num не число, то num вернется без изменений, т.к. отработает блок try/except
       Если num может быть переведен в число, то делим его на дробную и целую часть."""

    try:
        if int(float(num)):
            float_part, int_part = modf(float(num))
            if float_part:
                return str(float(num))
            return str(int(int_part))
        return 'Error in weight'
    except:
        return num


def get_date_time() -> Tuple[str, ...]:
    year, month, date = datetime.now().strftime('%Y_%m %M_%d.%m.%Y').split('_')
    return year, month, date


def rename_df_header(df: DataFrame) -> DataFrame:
    df.rename(columns=analytycal_sample_header, inplace=True)
    return df


def task_rw_df_to_lable_df() -> DataFrame:
    # Получаем датафрейм
    df = get_df()
    # Переименовываем названия колонок
    df = rename_df_header(df)
    # Добавляем информацию о терминале в строку к клиенту
    df[LEXICON['Client']] = df[LEXICON['Client']] + '  ' + df[LEXICON['Terminal']]
    # Добавляем информацию о материале в строку к номеру лота (также если номер лота - int)
    # !!! пока не получилось: работает не стабильно + лот используется для генерации QR кода !!!
    # df[LEXICON['Lot #']] = df[LEXICON['Lot #']].map(str) + ' ' + df[LEXICON['Material']]
    # Упорядочиваем колонки в нужном порядке
    df = df[[LEXICON['Client'], LEXICON['Sampl. date'], LEXICON['Ex.'], LEXICON['Mark'],
             LEXICON['Reference'], LEXICON['Lot #'], LEXICON['Material'], LEXICON['Weight'],
             LEXICON['Prepared by'], LEXICON['Pulverized by'], LEXICON['Sampled by']]]
    # Вставляем колонку с датой печати и типом пробы
    ins = f'{get_date_time()[2]} Analytical sample'
    df.insert(loc=0, column='Date', value=ins, allow_duplicates=True)
    # Сбрасываем индекс таблицы
    df.reset_index(drop=True, inplace=True)
    # Обрабатываем столбец с датами: там где дата - переводим в форматированную строку,
    # там где диапазон - оставляем строку
    df['Sampl. date'] = df['Sampl. date'].apply(
        lambda x: x if isinstance(x, str) else x.strftime(format='%d/%m/%Y'))

    # Обрабатываем столбец с номерами лотов: там где число - переводим в int,
    # там где строка - оставляем строку, если float то возвращаем int
    df['Lot #'] = df['Lot #'].apply(lambda x: int(x) if isfloat(x) else x)
    # русские буквы заменяем на английские заглавные
    df['Lot #'] = df['Lot #'].apply(lambda x: translit(x.upper(), language_code='ru', reversed=True) if isinstance(x, str) else x)


    # Обрабатываем столбец с весами лотов: там где число с дробной частью отличной от 0 -
    # переводим в int, там где строка - оставляем строку
    df['Weight'] = df['Weight'].apply(lambda x: check_weight(x))

    # Обрабатываем столбец Sampled - заменяем '\n' на '\'
    # df['Sampled'] = df['Sampled'].apply(lambda x: x.replace('\n', '\\'))

    # Заменяем NaN на '-'
    df.fillna(value='-', inplace=True)

    return df


def main():
    pd.set_option('display.max_columns', None)
    df = task_rw_df_to_lable_df()
    df.info()
    print(df.head(20))


if __name__ == '__main__':
    main()
