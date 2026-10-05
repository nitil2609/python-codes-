a = input("enter the string=")
b = ""
for i in range(len(a)-1,-1,-1):
  b = b + a[i]
if b == a:
    print(" pallendrome")
else :
    print("not pallendrome")
