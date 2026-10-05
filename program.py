# largest number between three numbers
a = int (input("enter the first number "))
b = int (input ("enter the second number "))
c = int (input ("enter the third number "))

if a>b and a>c :
    print (F"{a} is the largest ")
elif b>c and b>a:
    print(f"{b} is largest")
else:
    print(f"{c} is largest")


