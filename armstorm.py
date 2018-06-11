n=int(input("enter a number"))
num=n
p=0
while n>0:
    n=n//10
    p=p+1
n=num
s=0
while n:
    r=n%10
    n=n//10
    s=s+r**p
if s==num:
    print("armstorm")
else:
    print("not armstorm") 



 

