def fact(num):
    if num == 1:
        return num
    else:
        return num*fact(num-1)
num = int(input("enter the number to find the factorial:"))
if num<0:
    print("factorial is not allowed for negative numbers")
elif num == 0:
    print("factorial of the number 0 is 1")
else:
    print("factorial of",num, "is:",fact(num))