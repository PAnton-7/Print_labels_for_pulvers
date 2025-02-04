from lexicon import LEXICON

def lable_code(tsclibrary, one_label_dict):
    """
    14. windowsfont(a,b,c,d,e,f,g,h)
    Description: Use Windows font to print text
    Parameter:
    a: Integer, the starting point of the text along the X direction, given in dots
    b: Integer, the starting point of the text along the Y direction, given in dots
    c: Integer, the font height, given in points.
    d:Integer, rotation in counter clockwise direction
    0 -> 0 degree
    90-> 90 degree
    180-> 180 degree
    270-> 270 degree
    e: Integer, font style
    0-> Normal
    1-> Italic
    2-> Bold
    3-> Bold and Italic
    f: Integer, font with underline
    1-> Without underline
    g: String, font type face. Specify the true type font name. For example: Arial,
    Times new Roman.
    h: String, text to be printed

    :param tsclibrary:
    :return:
    """

    # Задаем данные печати: параметры шрифта, печати, отступы
    # fontstyle:
    normal, italic, bold = 0, 1, 2
    rotation, underline = 0, 0
    font = "Tahoma"

    X = 25  # Отступ от левого края

    tsclibrary.windowsfontW(f'{X}', f'{0}', f'{25}', f'{rotation}', f'{bold}',  # Дата
                            f'{underline}', f'{font}', f'Date   {one_label_dict[LEXICON["Date"]]}')
    tsclibrary.windowsfontW(f'{X}', f'{25}', f'{25}', f'{rotation}', f'{normal}',  # Клиент
                            f'{underline}', f'{font}', f'Client {one_label_dict[LEXICON["Client"]]}')
    tsclibrary.windowsfontW(f'{X}', f'{50}', f'{29}', f'{rotation}', f'{normal}',  # Дата отбора
                            f'{underline}', f'{font}', f'Sampl. date   {one_label_dict[LEXICON["Sampl. date"]]}')
    tsclibrary.windowsfontW(f'{X}', f'{75}', f'{32}', f'{rotation}', f'{normal}',  # Источник
                            f'{underline}', f'{font}', f'Ex.    {one_label_dict[LEXICON["Ex."]]}')
    tsclibrary.windowsfontW(f'{X}', f'{100}', f'{32}', f'{rotation}', f'{normal}',  # Марка
                            f'{underline}', f'{font}', f'Mark   {one_label_dict[LEXICON["Mark"]]}')
    tsclibrary.windowsfontW(f'{X}', f'{125}', f'{36}', f'{rotation}', f'{bold}',  # Реф
                            f'{underline}', f'{font}', f'Reference     {one_label_dict[LEXICON["Reference"]]}')
    tsclibrary.windowsfontW(f'{X}', f'{150}', f'{36}', f'{rotation}', f'{bold}',  # Лот
                            f'{underline}', f'{font}', f'Lot #  {one_label_dict[LEXICON["Lot #"]]}')
    tsclibrary.windowsfontW(f'{X}', f'{175}', f'{25}', f'{rotation}', f'{normal}',  # Материал
                            f'{underline}', f'{font}', f'Material      {one_label_dict[LEXICON["Material"]]}')
    tsclibrary.windowsfontW(f'{X}', f'{200}', f'{36}', f'{rotation}', f'{bold}',  # Вес
                            f'{underline}', f'{font}', f'Weight        {one_label_dict[LEXICON["Weight"]]}')
    tsclibrary.windowsfontW(f'{X}', f'{225}', f'{25}', f'{rotation}', f'{bold}',  # Подготовил
                            f'{underline}', f'{font}', f'Prepared by   {one_label_dict[LEXICON["Prepared by"]]}')
    tsclibrary.windowsfontW(f'{X}', f'{250}', f'{25}', f'{rotation}', f'{bold}',  # Пульверил
                            f'{underline}', f'{font}', f'Pulverized by {one_label_dict[LEXICON["Pulverized by"]]}')
    tsclibrary.windowsfontW(f'{X}', f'{275}', f'{25}', f'{rotation}', f'{bold}',  # Отобрал
                            f'{underline}', f'{font}', f'Sampled       {one_label_dict[LEXICON["Sampled by"]]}')

def lable_like_excel_code(tsclibrary, one_label_dict):
    # Задаем данные печати: параметры шрифта, печати, отступы
    # fontstyle:
    normal, italic, bold = 0, 1, 2
    rotation, underline = 0, 0
    font = "Tahoma"

    header_font_size = 25

    X0 = 1   # 0 мм - отступ от левого края
    X = 130  # 16 мм - отступ от левого края

    tsclibrary.windowsfontW(f'{X0}', f'{0}', f'{header_font_size}', f'{rotation}', f'{normal}',  # Дата
                            f'{underline}', f'{font}', f'Date')
    tsclibrary.windowsfontW(f'{X}', f'{0}', f'{25}', f'{rotation}', f'{bold}',  # Дата
                            f'{underline}', f'{font}', f'{one_label_dict[LEXICON["Date"]]}')

    tsclibrary.windowsfontW(f'{X0}', f'{25}', f'{header_font_size}', f'{rotation}', f'{normal}',  # Клиент
                            f'{underline}', f'{font}', f'Client')
    tsclibrary.windowsfontW(f'{X}', f'{25}', f'{25}', f'{rotation}', f'{normal}',  # Клиент
                            f'{underline}', f'{font}', f'{one_label_dict[LEXICON["Client"]]}')

    tsclibrary.windowsfontW(f'{X0}', f'{50}', f'{header_font_size}', f'{rotation}', f'{normal}',  # Дата отбора
                            f'{underline}', f'{font}', f'Sampl. date')
    tsclibrary.windowsfontW(f'{X}', f'{50}', f'{29}', f'{rotation}', f'{bold}',  # Дата отбора
                            f'{underline}', f'{font}', f'{one_label_dict[LEXICON["Sampl. date"]]}')

    tsclibrary.windowsfontW(f'{X0}', f'{75}', f'{header_font_size}', f'{rotation}', f'{normal}',  # Источник
                            f'{underline}', f'{font}', f'Ex.')
    tsclibrary.windowsfontW(f'{X}', f'{75}', f'{32}', f'{rotation}', f'{bold}',  # Источник
                            f'{underline}', f'{font}', f'{one_label_dict[LEXICON["Ex."]]}')

    tsclibrary.windowsfontW(f'{X0}', f'{100}', f'{header_font_size}', f'{rotation}', f'{normal}',  # Марка
                            f'{underline}', f'{font}', f'Mark')
    tsclibrary.windowsfontW(f'{X}', f'{100}', f'{32}', f'{rotation}', f'{normal}',  # Марка
                            f'{underline}', f'{font}', f'{one_label_dict[LEXICON["Mark"]]}')

    tsclibrary.windowsfontW(f'{X0}', f'{125}', f'{header_font_size}', f'{rotation}', f'{normal}',  # Реф
                            f'{underline}', f'{font}', f'Reference')
    tsclibrary.windowsfontW(f'{X}', f'{125}', f'{36}', f'{rotation}', f'{bold}',  # Реф
                            f'{underline}', f'{font}', f'{one_label_dict[LEXICON["Reference"]]}')

    tsclibrary.windowsfontW(f'{X0}', f'{150}', f'{header_font_size}', f'{rotation}', f'{normal}',  # Лот
                            f'{underline}', f'{font}', f'Lot #')
    tsclibrary.windowsfontW(f'{X}', f'{150}', f'{36}', f'{rotation}', f'{bold}',  # Лот
                            f'{underline}', f'{font}', f'{one_label_dict[LEXICON["Lot #"]]}')

    tsclibrary.windowsfontW(f'{X0}', f'{175}', f'{header_font_size}', f'{rotation}', f'{normal}',  # Материал
                            f'{underline}', f'{font}', f'Material')
    tsclibrary.windowsfontW(f'{X}', f'{175}', f'{25}', f'{rotation}', f'{normal}',  # Материал
                            f'{underline}', f'{font}', f'{one_label_dict[LEXICON["Material"]]}')

    tsclibrary.windowsfontW(f'{X0}', f'{200}', f'{header_font_size}', f'{rotation}', f'{normal}',  # Вес
                            f'{underline}', f'{font}', f'Weight')
    tsclibrary.windowsfontW(f'{X}', f'{200}', f'{36}', f'{rotation}', f'{bold}',  # Вес
                            f'{underline}', f'{font}', f'{one_label_dict[LEXICON["Weight"]]}')

    tsclibrary.windowsfontW(f'{X0}', f'{225}', f'{header_font_size}', f'{rotation}', f'{normal}',  # Подготовил
                            f'{underline}', f'{font}', f'Prepared by')
    tsclibrary.windowsfontW(f'{X}', f'{225}', f'{25}', f'{rotation}', f'{bold}',  # Подготовил
                            f'{underline}', f'{font}', f'{one_label_dict[LEXICON["Prepared by"]]}')

    tsclibrary.windowsfontW(f'{X0}', f'{250}', f'{header_font_size}', f'{rotation}', f'{normal}',  # Пульверил
                            f'{underline}', f'{font}', f'Pulverized by')
    tsclibrary.windowsfontW(f'{X}', f'{250}', f'{25}', f'{rotation}', f'{bold}',  # Пульверил
                            f'{underline}', f'{font}', f'{one_label_dict[LEXICON["Pulverized by"]]}')

    tsclibrary.windowsfontW(f'{X0}', f'{275}', f'{header_font_size}', f'{rotation}', f'{normal}',  # Отобрал
                            f'{underline}', f'{font}', f'Sampled')
    tsclibrary.windowsfontW(f'{X}', f'{275}', f'{25}', f'{rotation}', f'{bold}',  # Отобрал
                            f'{underline}', f'{font}', f'{one_label_dict[LEXICON["Sampled by"]]}')
