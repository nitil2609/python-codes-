l = [12, 23, 34, 45, 56,128, 67, 78, 89, 90]
greatest = l[0]
index = 0
for i in range(len(l)):

    if greatest < l[i]:
        greatest = l[i]
        index = i
print(f"greatest num is {greatest} at index {index}")
       

