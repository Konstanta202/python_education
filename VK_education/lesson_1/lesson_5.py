def fun_count_players(n):
    count = 0
    while (n != 1) :
        if (n % 2 == 0):
            count += 1
        n -= 1
    return count

print(fun_count_players(36))
