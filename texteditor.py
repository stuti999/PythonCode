import os
import sys
import shutil
def read():
    f=input("Enter a full path")
    if os.access(f,os.F_OK) and os.access(f,os.R_OK):
        f=open(f)
        data = f.read()
        f.close()
        print("Here is your data")
        print(data)

        main()
    else:
        print("Either Path invalid or Permission Error ")
        print("Try again")

def write():
    f=input("Enter full path:")
    f=open(f,'w')
    print("type : wq to save file\n\n")
    while True:
        d=input()
        if d.lower() ==":wq":
            f.close()
            break
        f.write(d)
        f.write("\n")

def delete():
    f=input("enter your file name")
    os.unlink(f)
    print("your file has been deleted")
    Edit()
    
    
def new():
    f=("Enter a full path")
    f=open(f,w)
    print("new file is created")
    c_file()

def  rename():
    p1=input("enter current name of file")
    p2=input("enter a name you want to change")
    os.rename(p1,p2)
    print("file name is change")
    Edit()
    

def move():
    path1=input("Enter your current path")
    path2=input("enter your ditenation path")
    shutil.move(path1,path2)
    print("your file is move")
            
def Edit():
    print("menu")
    print("\n1.move\n2.replace\n3.delete")
    ch=int(input("Emter your choice:"))
    if ch==1:
        move()
    elif ch==2:
        rename()
    elif ch==3:
        delete()
    else:
        print("\n\nInvlid choice")
        Edit()
    
        
def c_file():
    print("menu")
    print("1.new\n2.read\n3.write")
    ch=int(input("enter your choice:"))
    if ch==1:
        new()
    elif ch==2:
        read()
    elif ch==3:
        write()
    else:
        print("\n\ninvalid choice")
        c_file()


def main():
    print("1.File\n2.Edit\n3.exit")
    ch=int(input("Enter your choice:"))
    if ch==1:
        c_file()
    elif ch == 2:
        Edit()
    elif ch== 3:
        exit(0)
    else:
        print("Invalid choice:")
        main()



if __name__=="__main__":
    main()
