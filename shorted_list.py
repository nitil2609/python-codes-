l = [45,76,89,90,93,96,99]

for i in range(len(l)-1):
    if l[i] < l[i+ 1]  :
        continue
    else :
        print ("yuor list is not shorted")

        break
else :
    print("your list is sorted")


    