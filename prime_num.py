n = int(input("enter the number="))

count = 0
for i in range(1,n+1):
    if n %i ==0:
        count =count +1
if count== 2:
    print("prime number")
else:
    print ("not prime")

# another logic to find prime number

n = int(input("enter the number ="))
sum = 0 
for i in range(1,n+1):
    if n%i ==0:
        sum = sum +i

if sum ==n+1:
     print(f"{n} is a prime number ")
else :
    print(f"{n} is not a prime number")