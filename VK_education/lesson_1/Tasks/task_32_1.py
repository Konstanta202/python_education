import string


def parcer(input_str):
    result = []
    words = input_str.split()
    if words and words[0][0] == '!':
        for word in words:
            word = word.upper()
            word = word.translate(str.maketrans('', '', "!@#%"))
            result.append(word)
    else:
        for word in words:
            word = word.lower()
            word = word.translate(str.maketrans('', '', "!@#%"))
            result.append(word)
    return result

arr_str = []
while True:
    input_str = input()
    if input_str == '':
        break
    arr_str.append(input_str)
for string in arr_str:
    print(" ".join(parcer(string)))