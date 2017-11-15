import requests


def translate_it(text, lang):
    """
    YANDEX translation plugin

    docs: https://tech.yandex.ru/translate/doc/dg/reference/translate-docpage/

    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]

    :param text: <str> text for translation.
    :return: <str> translated text.
    """
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    key = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'

    params = {
        'key': key,
        'lang': lang,
        'text': text,
    }
    response = requests.get(url, params=params).json()
    return ' '.join(response.get('text', []))


def read_text(file):
    with open(file, encoding='utf-8') as f:
        text = f.read()
        return text


def program():
    language = ['de', 'es', 'fr', 'en', 'ru']
    print('введите номер документа')
    print('1 - DE.txt')
    print('2 - ES.txt')
    print('3 - FR.txt')
    file = input('введите число')
    if file == '1':
        text = read_text('DE.txt')
    elif file == '2':
        text = read_text('ES.txt')
    elif file == '3':
        text = read_text('FR.txt')
    print('выберите язык, с которого перевести')
    print('1 - немецкий')
    print('2 - испанский')
    print('3 - французкий')
    print('4 - английский')
    print('5 - русский')
    language_in = input('введите число')
    if language_in == '1':
        language_in = language[0]
    elif language_in == '2':
        language_in = language[1]
    elif language_in == '3':
        language_in = language[2]
    elif language_in == '4':
        language_in = language[3]
    elif language_in == '5':
        language_in = language[4]
    print('выберите язык, на который перевести(русский по умолчанию)')
    print('1 - немецкий')
    print('2 - испанский')
    print('3 - французкий')
    print('4 - английский')
    language_out = input('введите число или enter')
    if language_out == '1':
        language_out = language[0]
    elif language_out == '2':
        language_out = language[1]
    elif language_out == '3':
        language_out = language[2]
    elif language_out == '4':
        language_out = language[3]
    elif language_out == '':
        language_out = language[4]
    lang = language_in + '-' + language_out
    with open('translate_output.txt', 'a', encoding='utf-8') as f:
        f.write(translate_it(text, lang))
        f.write('\n')
    print('перевод находится в файле translate_output.txt')
    program()


program()
