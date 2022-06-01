

def read_template(string):
    """ This function opens the file and reads content"""

    import os

    if os.path.exists(string):
        with open(string, 'r') as f:
            contents = f.read()
            return contents
    raise FileNotFoundError("File/path does not exist")


def parse_template(string):
    """ This function parses the information - story without user input and user input type"""
    import re

    text_in_curly = (re.findall('{(.+?)}', string))

    words_extract = list(text_in_curly)

    new_string = string
    for word in words_extract:
        new_string = new_string.replace(word, '')

    if new_string != string:
        return new_string, tuple(text_in_curly)


def merge(a, b1):
    """ This function merges the information - story  and user input"""
    import re

    words = a.split()
    i = 0
    c = 0
    while i < len(words):
        if re.search("{}", words[i]) and c < len(b1):
            words[i] = words[i].replace('{}', b1[c])
            i += 1
            c += 1
        elif c < len(b1):
            i += 1
        else:
            break

    if words != a:
        new_string2 = ' '.join(words)
        return new_string2


if __name__ == '__main__':
    print(
        """In this game we complete a story using the words you share. We only share the story after you give us
    the words to complete it. Since you don’t know what the story’s about, the result is a funny story.
    """)

    contents1 = read_template(
        '../assets/make_me_a_video_game_template.txt')
    story = parse_template(contents1)

    print(""" Please enter the information requested below""")

    Num_of_Entries = len(story[1])

    i1 = 0
    b = []

    while i1 < Num_of_Entries:
        x = input(" Enter " + story[1][i1] + " >")
        b.append(x)
        i1 += 1

    print(""" 
    
    Please see the funny story you created below

    """)

    funny_story = merge(story[0], b)

    print(funny_story)

    with open('../assets/my_story.txt', 'w') as f2:
        f2.write(funny_story)
