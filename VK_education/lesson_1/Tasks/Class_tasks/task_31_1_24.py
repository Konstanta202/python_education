class Counter:

    def __init__(self, initial_count):
        self.initial_count = initial_count

    def increment(self):
        self.initial_count += 1

    def get(self):
        return self.initial_count

code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)