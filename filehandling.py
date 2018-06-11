path=input("enter your path")
a=input()
while a!="wq":
    fp=open("path","w")
    fp.write(a)
    a=input()
fp.close()    
    
