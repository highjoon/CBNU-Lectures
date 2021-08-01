def edit(word_list, editor):
    return [editor(word) for word in word_list]


def to_upper(word):
    return word.upper()


wl = ['aaa', 'bbb', 'ccc']
result1 = edit(wl, to_upper)
result2 = edit(wl, lambda word: word.upper())
print(result1)
print(result2)