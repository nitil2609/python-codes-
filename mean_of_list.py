l = [12,23,34,45,56,67,78,89,90]
sum = 0
for i in range(len(l)):
    sum = sum + l[i]
mean = sum / len(l)
print(f"mean of list is {mean}")