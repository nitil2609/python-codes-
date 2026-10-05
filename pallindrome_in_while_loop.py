a= int(input("enter the num="))
copy = a 
rev =0
while a>0:
    rev = rev*10 + a%10
    a= a//10
if rev == copy:
    print("pallindrome number")
else:
    print("not pallindrome number")