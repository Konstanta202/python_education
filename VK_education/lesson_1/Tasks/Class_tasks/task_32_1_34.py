numerator, denominator = int(input()), int(input())
def changed_div(numerator, denominator):
    try:
        return float(numerator / denominator)
    except ZeroDivisionError:
        return 0
        # return denominator
print(changed_div(numerator, denominator))