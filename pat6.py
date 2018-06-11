n=int(input("enter no rows"))
for row in range (1,n+1):
    for col in range (1,n-row+1+1):
        print("*",end="")
    for col in range (1,2*row-2+1):
        print(" ",end="")
    for col in range (1,n-row+1+1):
        print("*",end='')            
    print()    
for row in range (1,n+1):
    for col in (1,row+1):
        print ("*",end="")
    for col in range (1,2*(n-row)+1):
        print(" ",end="")
    for col in range (1,row+1):
        print("*",end="")
    print()    
    
