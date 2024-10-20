import string
str = input()
str = str.lower()
words = str.split()
three = dict()
for word in words:
    punctuation = string.punctuation
    word = word.translate(str.maketrans('', '', punctuation))
    if len(word) >= 5:
        dict_ = dict()
        for char in word:
            dict_[char] = 0
        if len(dict_) >= 4:
            if word in three:
                three[word] += 1
            else:
                three[word] = 1
        dict_.clear()
result = {k for k, v in three.items() if v > 2}
for i in sorted(result):
    print(i)
