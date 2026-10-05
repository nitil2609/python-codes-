d1 = {1:12,2:32,3:33}
d2 = {5:66,6:56,7:73}
d1.update(d2)
print(d1)

#we can also do by using loop 

for i in d2:
    d1[1] = d2[i]
print(d1)
