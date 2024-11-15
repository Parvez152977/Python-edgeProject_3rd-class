def factorialOfN(n):
    if n == 0 or n == 1:
        return 1
    fact = factorialOfN(n-1) * n
    return fact
result=factorialOfN(4)
print(result)