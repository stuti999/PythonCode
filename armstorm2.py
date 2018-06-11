num= int(input("enter a number"))
temp= num
p=0
while num:
    num= num// 10
    p = p+1
x=0
num =temp
while num:
    r=num%10
    x=x+r**p
    num=num//10
if temp==x:
    print("no is aarmstorm")
else:
    print("not armstorm")


  

