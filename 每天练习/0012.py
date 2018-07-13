with open(r'filtered_words.txt', 'r', encoding='utf-8') as f:
    L = []
    for line in f.readlines():
        L.append(line.strip())


def changeBadWord(word):
    for badWord in L:
        if badWord in word:
            new_word = word.replace(badWord, '*'*len(badWord))
            return print(new_word)
    return print('all good')


word = input('请输入：')
changeBadWord(word)
