n,m=map(int,input("enter matric dimension:").lower().split("x"))
l=[]
h=[]
for i in range(n):
    a=list(map(int,input().split()))
    l.append(a)
print(l)        
for j in range (m):
    c=list(map(int,input().split()))
    h.append(c)
print(h)
print("matric A")
for i in range (n):
    for j in range (m):
        print(l[i][j],end'')
print(l)
print("Matric B")
for i in range (n):
    for j in range (m):
        print(h[i][j],end'')
print(h) 
    

