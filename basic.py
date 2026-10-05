#print("hello nitil")
"""a=12 
b=12.13
c=12j
print(type(a))"""


"""h = 'adf56655'
print(type(h)) 
string"""

'''a = " nitil kumar "
print(a[0:8:1])  # slicing of string'''

#type conversion
a=12
#a=str(a)
#print(type(a))

#print(bool(a))

'''a=14

print (14/2) explicit type conversion'''

#output 
#print (12)
#print is used to display output on the screen

#formated_string 
#print(f"my name is {n} and my age is {a}")

#age= input("hello my age is a")
#print = age 


#age = int (input("what is your age "))
#print ("age",age )

'''a = int(input("enter the num"))
b = int(input('enter the num'))
print("value of a and b before swapping")
print("value of a",a)
print("value of b ",b)

c= a 
a= b
b=c
print( "value of a and b after swapping")
print("value of a",a)
print("value of b",b)'''


'''a =int(input ("enter the num ="))
b =int(input ("enter the num ="))
print("value before swapping ")
print("value of a=",a)
print("value of b=",b)
a=a+b
b=a-b
a=a-b
print ("value after swapping")
print("value of a=",a)
print("value of b=",b)'''

"""a= 4
print("type of a",type(a))
b=12.3
print("type of b:",type(b))

c = 2+3J 
print("type of c:", type(c))"""





'''str2= "goat"
str1 = "nitil kumar"
print(str2+str1)'''

'''a= float(input("enter the num="))
area = a*a

perimeter = 4*a
print ("area of square is ",area )
print("perimete of square",perimeter)'''

'''a= int(input("enter the num="))
if a%2==0:
    print("even num")
else:
    print("odd num")'''

'''a = int(input("enter the num="))
b = int(input("enter the num="))
c = int(input("enter thr num="))

if a>b and a>c:
    print("a is greater")
elif b>a and b>c:
    print("b is greater")
else:
    print("c is greater") ''' 

'''a= int(input("enter the first num=\n"))
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
    print ("not involved in tje operation")'''

'''x = int (input('enter the num='))
if x%4==0:
    print ("leap year")
else :
    print("not leap year")'''

'''str1 = "nitil"
str2= " kumar"
print(str2 + " " +str1)'''

'''from datetime import date
firstday= date (2024,1,1)
lastday= date (2024,12,31)
diff= lastday-firstday
print("total days in year 2024 is",diff.days)'''

'''a =6667
print(chr(a))'''

'''a = int(input("enter the num="))
b = int(input("enetr the num="))

if a>b:
    print("a is greater")
else:
    print("b is greater")'''



'''a= input("enter the gender=")
if a== "male" :
    print("goood morning sir ")
elif a=="female":
    print("good morning mam")
else :
    print("other gender")'''


'''a= int(input('enter the num='))
if a%2==0:
    print("even num")
else:
    print("odd num")'''



'''name = str (input("name of the person="))
age =int(input("enter the age ="))
if age >18:
    print(f"{name } can vote")
else :
    print(f"{name} can't vote")

a = age -18 
if a>0:
    print(f"{name} can vote")'''
    


'''year = int(input("enter the year="))

if year%4==0 and year %400==0:
    print("leap year")
else:
    print("not leap year")'''


'''a = range(17,0,-1)

for i in a:
    print(i)


a = range(20,51,1)

for i in a:
    print(i)


a = range(-3,-16,-1)

for i in a:
    print(i)

a = range(5,51,5)

for i in a:
    print(i)

a = range(20,,1)

for i in a:
    print(i)'''


'''n = int (input ("enter the table number="))
for i in range(n,n*10+1,n):
    print(i)'''

'''a ="adfbob"
for i in range(6):
    print(a[i])'''

'''a = "bdbvhroevo"

print(len(a))
for i in range(len(a)):
     print(a[i])'''

'''for i in range(1,21):
     if i == 14:
          break
     print(i)


for i in range(1,21):
     if i == 14:
        continue
     print(i)'''

'''for i in range(1,21):
     if i == 14:
        print("break statement is exacuted")
        break
     print(i)
else:
    print("break statement is not exacuted")'''

'''n = int(input("enter the num="))
for i in range (n):
    print("hello nitil")'''

'''n = int(input("enter the num="))
for i in range (n+1):
    print (i)'''

'''n = int(input("enter the num="))
for i in range (n,0,-1):
    print(i)'''

'''n = int(input("enter the num="))
for i in range(n,n*10+1,n):
    print(i)'''

'''n=int(input("enter the num="))
sum =0
for i in range (1,n+1):
    sum = sum + i
print(f"sum of n numbers is {sum}")'''


'''n = int(input("enter the number="))
factorial = 1 
for i in range (n,0,-1):
    factorial = factorial * i
print(f"factorial of {n} is {factorial}")'''



'''n = int (input("enter the num="))
even_sum = 0
odd_sum = 0
for i in range (1,n+1):
    if i in range (2,1+n,2):
        even_sum = even_sum + i
    else :
        odd_sum = odd_sum + i
print(f"sum of even numbers is {even_sum}")
print(f"sum of odd numbers is {odd_sum}")'''


'''n= int(input("enter the number="))
factor = 1
sum =0 
for i in range (n, 0 ,-1):
    if n%i ==0:
        print(f"factors are {i}  ")'''


'''n = int (input("enter the number ="))

sum =0
for i in range (1 , n):
    if n%i == 0:
        sum = sum + i
if sum ==n:
    print (f"{n} is perfect number ")
else :
    print (f"{n} is not perfect number")'''


'''n = int(input("enter the number ="))
sum = 0 
for i in range(1,n+1):
    if n%i ==0:
        sum = sum +i

if sum ==n+1:
     print(f"{n} is a prime number ")
else :
    print(f"{n} is not a prime number")'''



'''a = int(input("enter the number ="))
if a% 2 == 0:
    print("num is even ")
else : print (" num is odd ")'''

      

    













    
