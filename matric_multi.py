n,m=map(int,input("enter matric dimension m n:").lower().split())
def show(X):
    for var in X:
        s='{:10)}'*len(var)
        print('\t',s.format(*var))
def mul(A,B):
    for i in range(len(A)):
        for j in range(len(B[0])):
            for j in range(len(B)):



print("matric A:")
print("matric A:")
A=[list(map(int,input('\t').split())) for var in range(n) ]
print("matric B:")
B=[list(map(int,input('\t').split())) for var in range(n) ]
print("Matric A is:")
show(A)
print("Matric B is:")
show(B)






        
