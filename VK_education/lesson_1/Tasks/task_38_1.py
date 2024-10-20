count = int(input())
max_value = []
while True:
    try:
        n = input()
        if count > 0:
            if n:
                tmp_ = list(map(int, n.split()))
                max_value.append(max(tmp_))
                count -= 1
    except EOFError:
        break

max_value.sort(reverse=True)
print(";".join(map(str, max_value)))
