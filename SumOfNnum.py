def sumOfNnum(n):
    if n == 0:
        return 0
    sum = n + sumOfNnum(n - 1)
    return sum

print(sumOfNnum(5))