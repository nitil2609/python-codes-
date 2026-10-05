l = [12, 31 ,34,56,37,78,89,70]



greatest = l[0]
sec_greatest = l[0]


for i in  l :
    if i > greatest :
        sec_greatest = greatest
        greatest = i

    elif i > sec_greatest:
        sec_greatest = i

print (sec_greatest, greatest)
