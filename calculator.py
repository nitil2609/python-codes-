a= int(input("enter the first num=\n"))
b = int(input("enter the second num=\n")) 
z =input("enter any one +,-,*,/,%,//\n") 

if z =="+":
    print("sum=",a+b)
elif z=="-":
    print("sub=",a-b)
elif z=="*":
    print("mul=",a*b)
elif z=="/":
    print("div=",a/b)
elif z=="//":
    print("floor div=",a//b)
elif z=="%":
    print("modulus=",a%b)
else:
    print ("not involved in tje operation")