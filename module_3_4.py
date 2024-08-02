def single_root_words(root_word, *other_words):
    root_word = root_word.lower()
    other_words_lower = [s.lower() for s in other_words]
    same_words = []
    for i in range(len(other_words)):
        if root_word in other_words_lower[i] or other_words_lower[i] in root_word:
            same_words.append(other_words[i])
    return same_words
print(single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies'))
print(single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))
