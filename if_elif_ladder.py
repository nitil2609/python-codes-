temperature = int(input("enter the temperature ="))
if temperature < 0:
    print("freezing cold")

elif temperature >= 0 and temperature < 10:
    print("very cold")
    
elif temperature >= 10 and temperature < 20:
    print("cold")

elif temperature >= 20 and temperature <30:
    print("pleasant")

elif temperature >= 30 and temperature > 40:
    print("hot")

else:
    print("very hot")