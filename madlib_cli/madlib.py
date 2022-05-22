def read_template(string):
    with open(string, 'r') as f:
        content = f.read()
        return content


def parse_template(string):
    import re

    text_in_curly = (re.findall('{(.+?)}', string))

    words_extract = set(text_in_curly)

    new_string = string
    for word in words_extract:
        new_string = new_string.replace(word, "")

    if new_string != string:
        return '"'+new_string+'"', tuple(text_in_curly)

    # stripped = '"'+new_string+'"'
    # parts = tuple(text_in_curly)

    # print(_stripped, _parts)


def merge(string):
    pass
