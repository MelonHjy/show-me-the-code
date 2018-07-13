with open(r'filtered_words.txt', 'r', encoding='utf-8') as f:
    L = []
    for line in f.readlines():
        L.append(line.strip())


def filter_word(word):
    for filterWord in L:
        if filterWord in word:
            return print('Freedom')
    return print('Human Rights')


word = input('请输入：')
filter_word(word)
