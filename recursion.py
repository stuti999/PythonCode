def sum(a):
    if a==1:
        return 1
    else:
        a+sum(a-1)
print(sum(int(input("enter a number:")))) 
new=lambda x: 1 if x==1 else x+new(x-1)

print(sum(int(input("enter a number:")))) 
