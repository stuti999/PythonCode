n=int(input("enter a number of row"))
for row in range (1,n+1):
    for col in range (1,n-row+1):
        print(" ",end="")
    for col in range (1,row+1):
            print("*",end="")
    print()        
