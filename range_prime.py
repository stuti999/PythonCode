n= int(input ("starting point"))
e= int(input ("ending point"))
s=2
e=num - 1
while s<=e:
    if num % s==0:
     f="not prime"
     print("given {} is not a prime number.".format(num))
     break
    else:
        f="may be prime"
    s = s+1
if f=="may be prime":
    print("given {} is prime Number.".format(num))
    



     

