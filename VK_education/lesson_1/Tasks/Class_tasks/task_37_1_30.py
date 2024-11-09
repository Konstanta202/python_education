class Dictionary:
    def __init__(self, dictionary):
        self._dictionary = dictionary

    def __call__(self, key):
        return self._dictionary.get(key)

code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)

