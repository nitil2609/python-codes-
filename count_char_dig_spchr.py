a ="jy73r23f$%3"

char =0
dig =0
spchr =0

for i in a:
    if i.isdigit():
        dig = dig +1
    elif i.isalpha():
        char = char +1
    else: 
        spchr = spchr +1
    print (f"your digits are {dig}\nyour alphabets are {char}\nyour special character are {spchr}")