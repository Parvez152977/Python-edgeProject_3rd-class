def recursiveNum(number):
    if number == 0:
        return
    print(number,end=" ")
    recursiveNum(number-1)
recursiveNum(int(input("Enter The number: ")))