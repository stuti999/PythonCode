s=int(input("enter start point"))
e=int(input("ending point"))
for n in range(s,e+1):
 num=n
 p=i0
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
    print(num,end='\t') 



 

