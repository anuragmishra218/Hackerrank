def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']


def score_words(words):
    score = 0
    for i in words:
        count = 0
        for j in i:
            if is_vowel(j):
                count += 1
        if count % 2 == 0:
            score += 2
        else:
            score += 1

    return score


n = 3
w = 'programming is awesome'
words = w.split()
print(score_words(words))
