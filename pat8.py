n=int(input('enter  no of row :'))
for row in range(1,n+1):
    c=65
    for col in range(1,row+1):
        
       print(chr(c),end="")
       c=c+1
    print()


