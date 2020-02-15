a=1
for i in range(100):
    if a%7==0:
        a+=1
        continue
    elif a%10==7:
        a+=1
        continue
    elif a//10==7:
        a+=1
        continue
    else:
        print(a)
        a+=1
#哼哼哼！
