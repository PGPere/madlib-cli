"""
In this game we complete a story using the words you share. We only share the story after you give us
the words to complete it. Since you don’t know what the story’s about, the result is a funny story.
"""


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
        return new_string, tuple(text_in_curly)


def merge(a, b):
    import re

    words = a.split()
    i = 0; c = 0
    while i < len(words):
        if re.search("{}", words[i]) and c < len(b):
            words[i] = words[i].replace('{}', b[c])
            i += 1
            c += 1
        elif c < len(b):
            i += 1
        else:
            break

    if words != a:
        new_string2 = ' '.join(words)
        return new_string2
