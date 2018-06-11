l1=[]
l2=[]
l3=[]
l4=[]
l5=[]
for var in range(1,5+1):
    n=input("enter your name")
    m=float(input("enter your marks"))
    if var==1:
        l1.append(n)
        l1.append(m)
    elif var==2:
       l2.append(n)
       l2.append(m)
        
    elif var==3:
        l3.append(n)
        l3.append(m)
    elif var==4:
        l4.append(n)
        l4.append(m)
    else:
        l5.append(n)
        l5.append(m)
print(l1)
print(l2)
print(l3)
print(l4)
print(l5)


