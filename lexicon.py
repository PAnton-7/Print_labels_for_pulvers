# Английский язык
ENG_LEXICON = {'Sample': 'Sample',
               'Date': 'Date',
               'Client': 'Client',
               'Sampl. date': 'Sampl. date',
               'Ex.': 'Ex.',
               'Mark': 'Mark',
               'Reference': 'Reference',
               'Lot #': 'Lot #',
               'Material': 'Material',
               'Weight': 'Weight',
               'Train': 'Train',
               'Sampled by': 'Sampled',
               'Prepared by': 'Prepared by',
               'Pulverized by': 'Pulverized by',
               'RESERVE SAMPLE': 'RESERVE SAMPLE',
               'SIZE': 'SIZE',
               'For total moisture determ.': 'For total moisture determ.',
               'For prep. PHISICAL comp.': 'For prep. PHISICAL comp.',
               'For prep. LAB comp.': 'For prep. LAB comp.',
               'For pulverizing': 'For pulverizing',
               'Analytical sample': 'Analytical sample',
               'Coal': 'Coal',
               'Pet. Coke': 'Pet. Coke',
               'Coke': 'Coke',
               'Program': 'Program',
               'Shipper': 'Shipper',
               'Terminal': 'Terminal'}

# Русский язык
RUS_LEXICON = {'Sample': 'Проба',
               'Date': 'Дата',
               'Client': 'Клиент',
               'Sampl. date': 'Дата отбор.',
               'Ex.': 'Название',
               'Mark': 'Марка',
               'Reference': 'Референс',
               'Lot #': 'Лот №',
               'Material': 'Материал',
               'Weight': 'Вес',
               'Train': 'Состав',
               'Sampled by': 'Отобрал',
               'Prepared by': 'Подготовил',
               'Pulverized by': 'Пульверизовал',
               'RESERVE SAMPLE': 'РЕЗЕРВ',
               'SIZE': 'СИТОВЫЙ',
               'For total moisture determ.': 'Для опр. общ. влаги',
               'For prep. PHISICAL comp.': 'Для подг. ФИЗ комп.',
               'For prep. LAB comp.': 'Для подг. ЛАБ комп.',
               'For pulverizing': 'Для пульверизации',
               'Analytical sample': 'Аналит. проба',
               'Coal': 'Уголь',
               'Pet. Coke': 'Нефтекокс',
               'Coke': 'Кокс',
               'Program': 'Программа',
               'Shipper': 'Грузоотправитель',
               'Terminal': 'Терминал'}

# Выбор языка
LEXICON = ENG_LEXICON

# Словарь для переименования шапки задания на обработку для
# печати бирок на аналитические пробы
analytycal_sample_header = {'ПРОГРАММА СКЛАДИРОВАНИЯ': LEXICON['Program'],
                            'РЕФЕРЕНС': LEXICON['Reference'],
                            'ГРУЗООТПРАВИТЕЛЬ': LEXICON['Ex.'],
                            'МАРКА': LEXICON['Mark'],
                            'СИТОВЫЙ': LEXICON['SIZE'],
                            'ДАТА ОТБОРА': LEXICON['Sampl. date'],
                            'ВЕС': LEXICON['Weight'],
                            'СОСТАВ': LEXICON['Train'],
                            'ЛОТ №': LEXICON['Lot #'],
                            'ВЫПОЛНИЛ ОТБОР': LEXICON['Sampled by'],
                            'Обработку выполнил': LEXICON['Prepared by'],
                            'Пульверизацию выполнил': LEXICON['Pulverized by'],
                            'Клиент': LEXICON['Client'],
                            'терминал': LEXICON['Terminal'],
                            'материал': LEXICON['Material']
                            }

# #Попытка печати в цикле FOR. Неудачная, так как оказалось невозможно плавно регулировать высоту строк
# #Блок форматирования
# X, Y, font_height = 25, -15, 35
# rotation, style, underline = 0, 2, 0
# font = "Tahoma"


# if _[0] in [LEXICON['Client'], LEXICON['Data'], LEXICON['Material']]:
#     font_height, style = 22, 0
#     Y += 25
# elif _[0] in [LEXICON['Ex.'], LEXICON['Reference'], LEXICON['Lot #'],
#               LEXICON['Weight'], LEXICON['Sampl. date']]:
#     font_height, style = 35, 2
#     Y += 25
# else:
#     font_height, style = 30, 0
#     Y += 25
#
# #Печатаем
# tsclibrary.windowsfontW(f'{X}', f'{Y}', f'{font_height}', f'{rotation}', f'{style}', #Отобрал
#                       f'{underline}', f'{font}', f'{_[0]} {_[1]}')
