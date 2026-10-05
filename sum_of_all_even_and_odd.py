a = int(input("enter the number="))
sum_even =0
sum_odd =0

for i in range (1,a+1):
    if i%2==0:
        sum_even =sum_even +i
    else:
        sum_odd =sum_odd +i
print("sum of all even numbers=",sum_even)
print("sum of all odd numbers=",sum_odd)
