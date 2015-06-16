# -*- coding:utf-8 -*-
# coding=<utf8>

__version__ = '0.0.1'

import datetime, re

def what_to_people_friendly(a):
    """
    Функция для преобразования списка покупок в человеческий вид

    >>> a='a;a;b;a;b;a'
    >>> what_to_people_friendly(a)
    u'a - 4 \u0448\u0442; b - 2 \u0448\u0442; '
    """
    b=list(set(a.split(';')))
    c = ''
    for word in b:
        count=a.split(';').count(word)
        c = c + word + ' - ' + str(count) + u' шт; '
    return c

def strings_to_lower_with_first_upper(strings, field_number=0,
                                      separator=';'):
    """
    Получает список строк. Возвращает те же строки, где если каждую
    строку разбить по separator то поле с номером field_number будет
    переводится в нижний регистр
    Из
    АБВГД ЕЖЗИК ЛМ
    будет
    Абвгд Ежзик лм
    :param strings: список строк
    :param field_number: номер поля, по умолчанию - вся строка
    :param separator: разделитель полей, по умолчанию ';'
    :return: список строк
    """
    new_strings = []
    for string in strings:
        # если вся строка
        if not field_number:
            raise NotImplementedError(u"Пока не надо - не делал")
        else:
            str_tmp = string.split(separator)[field_number].split(' ')
            str_new = ''
            for a in str_tmp[:-1]:
                try:
                    str_new = str_new + a[0].upper()+a[1:].lower() + ' '
                except:
                    print('TO_LOW_ERR: '+string)
                    continue
            str_new += str_tmp[-1].lower()
            new_list = string.split(separator)[:field_number]
            new_list.append(str_new)
            new_list += string.split(separator)[field_number+1:]
            new_strings.append(separator.join(new_list))
    return new_strings

def htmlize(text):
    def make_html_table(text):
        """
        '\n       ||h1||h2||h1||h2||\n            ||r1||r2||r1||r2||'
        превращает в таблицу на html
        """
        html = u"<table border=1>"
        rows = re.findall(r'(^\s*\|\|.*\S+.*\|\|\s*$)',text,re.M)
        for row in rows:
            row_html = u"<tr>"
            cells = row.strip().split('||')[1:-1]
            #['h1', 'h2', 'h1', 'h2']
            for cell in cells:
                row_html +=u"<td>{0}</td>".format(cell)
            row_html += u"</tr>"
            html += row_html
        html += u"</table>"
        return html

    # список для замены, списки: (ключ, (значения))
    # ключь - шаблон для поиска
    # занчения - (шаблон для поиска для замены в исходной строке,
    #             шаблон для замены)
    escaped_tuple=((r'\\(*)',(u'\\*',u'???asterics???')),
                    (r'\\(\\)',(u'\\\\',u'???backslash???')),
                    (r'({)',(u'{',u'???curle_open???')),
                    (r'(})',(u'}',u'???curle_close???')),
                    )
    unescaped_tuple=((u'???asterics???',u'*'),
                    (u'???backslash???',u'\\'),
                    (u'???curle_open???',u'{'),
                    (u'???curle_close???',u'}'),
                    )

    replace_tuple=((r'\*\*([^*]*)\*\*',(u'**{0}**',
                                             u'<i>{0}</i>')),
                    (r'\*([^*]*)\*',(u'*{0}*',u'<b>{0}</b>')),
                    )

    # сперва мы заменим на временные последовательности все
    # экранированные символы, чтобы не мешались
    # \\([*\\])
    for template,replacement in escaped_tuple:
        # strings = re.findall(r'\\([*\\])',text)
        # for string in strings:
        text = text.replace(replacement[0],
                                replacement[1])
        # print text
    # print text
    text = text.replace(u'&',u'&amp')
    text = text.replace(u'<',u'&lt')
    text = text.replace(u'>',u'&gt')
    text = text.replace(u'\r\n',u'\n')
    for template,replacement in replace_tuple:
        strings = re.findall(template,text)

        # print (strings)
        for string in strings:
            text = text.replace(replacement[0].format(string),
                                replacement[1].format(string))
        # print text

            # ОБРАБОТКА ССЫЛОК
    # r'(https?://\S*)',('{0}','<a href="{0}">{0}</a>'))
    # ссылки придётся обрабатывать по хитрому. Сперва мы заменяем
    # ссылку на {№№}, занося то, на что надо заменить в список. А
    # затем форматируем полученную строку с подстановкой
    links = re.findall(r'(https?://\S*)',text)
    html_links = []
    # Преобразуем в множество, чтобы каждый url заменять только
    # один раз. Затем упорядочиваем по длине от длинного к
    # короткому, чтобы не было замещения внутри длинного URL
    links = sorted(list(set(links)), key = lambda x: -len(x))
    # print "links=",links
    for index, link in enumerate(links):
        text = text.replace(link,'{'+str(index)+'}')
        html_links.append(u'<a href="{0}">{0}</a>'.format(
            link.replace(u'&amp',u'&')))
    # print html_links
    text = text.format(*html_links)

            # ОБРАТОБКА ТАБЛИЦ
    # поступаем так же как с ссылками
    tables = re.findall(r'((?:(?:\n|\n\r)?\s*\|\|.*\S+.*\|\|\s*('
                        r'?:\n|\n\r)?)+)',text,re.M)
    html_tables = []
    for index, table in enumerate(tables):
        text = text.replace(table,u'{'+str(index)+u'}')
        html_tables.append(make_html_table(table))
    text = text.format(*html_tables)
            # ВСТАВКА ЭКРАНИРОВАННЫХ СИМВОЛОВ
    for escaped, unescaped in unescaped_tuple:
        text = text.replace(escaped,unescaped)

    return text
