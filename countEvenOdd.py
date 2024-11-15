def countEvenOdd(numbers):
    countEven = 0
    countOdd = 0
    for ele in numbers:
        if ele % 2 == 0:
            countEven+=1
        else: countOdd+=1
    if countEven > countOdd:
        print("Even is greater")
    elif countOdd > countEven:
        print("Odd is greater")
    else:
        print("Both are equal")
numbers = [12,11,23,22,43]
countEvenOdd(numbers)