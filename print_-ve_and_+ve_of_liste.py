l = [12,-12,34,-45,67,-89,90]
#l = int(input("enter the number of elements in list ="))
for   i in range(len(l)):
    if l[i] > 0:
        print(f"positive number is {l[i]}")
    else:
        print (f"negative of number is {l[i]}")