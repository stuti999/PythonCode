import getpass
import time
import json
with open("bank.db") as fp:
    bank = json.load(fp)
    fp.close()


def update():
    fp=open("bank.db",'w')
    json.dump(bank,fp)
    fp.close()


def profile(i):
    print("Welcome{}".format(bank['user'][i]).center(200,"*"))
    print("\n1.update Name")
    print("\n2.Delete Account")
    print("\n3.logout")
    ch=int(input("enter your choice:"))
    if ch==1:
        name=input("enter new name:")
        bank["name"][i]=name
        update()
        choice(i)
    elif ch==2:
        cp=getpass("enter current password:")
        if cp==bank[password][i]:
            np = getpass("enter New Password:")
            vp = getpass("confirm password:")
            if np == vp:
                bank['password'][i]=np
                update()
                print("Password Sucessfully Updated")
                main()
            else:
                print("password Incorrect")
                main()
        elif ch == 3:
            bank['name'].pop(i)
            bank['acc'].pop(i)
            bank['bal'].pop(i)
            bank['password'].pop(i)
            update()
            print("Bye Bye")
            print("Your account Sucessfully Deleted")
            main()
            



def chk_bal(i):
    print("Name=",bank['name'][i])
    print("Acc Number=",bank['acc'][i])
    print("balance =",bank['bal'][i])
    choice(i)



def cerdit(i):
    global bank
    print("\n\n Welcome to cerdit Services")
    amount=int(input("enter amount to deposite:"))
    bank['bal']['i']+=amount
    update()
    print("Now you have rs in your account\n{} credited sucessfully in your account".format(bank['bal'][i],amount))
    choice(i)


def debit(i):
    global bank
    print("\n\nWelome Debit services".center(300,"*"))
    if amount > bank['bal'][i]:
        print("\n\nInsufficient account to be withdraw\nyou have only{} rs in your account".format(bank['bal'][i]))
        print("\nTry Again")
        debit(i)

    else:
        bank['bal'][i]-= amount
        time.sleep(1)
        update()
        print("\n rupess withdraw from your account".format(amount))
        print("\nRemaning balance=",bank['bal'][i])
        choice(i)


def choice(i):
    print("Welcome {}".format(bank['name'][i]).center(200,"*"))
    print("\n\nMenu\n")
    print("1.debit\n2.creit\n3.statement\4.profil update\n5.logout")
    ch=int(input("Enter your choice"))
    if ch==1:
        debit(i)
    elif ch==2:
        credit(i)
    elif ch==3:
        chk_bal(i)
    elif ch==4:
        profile(i)
    else:
        print("Error: invalid choice \nTry again")
        choice(i)
def login():
    print("welcome to login".center(300,"*"))
    print("\n\n")
    acc=int(input("Login Id:"))
    password=getpass("password")        
    if acc in bank['acc']:
        i=bank['acc'].index(acc)
        if password==bank['password'][i]:
            print("******processing*******")
            choice[i]
        else:
            print("\n\nError wrong password try again:")
            login()
    else:
        print("\n\nNo such account Exit\n you should Signup\n\n")
        main()


def signup():
    name=input("\n\nEnter name:")
    time.sleep(1)
    password=getpass.getpass()
    time.sleep(1)
    bal=int(input("intial balance to deposit:"))
    time.sleep(1)
    acc=bank["acc"][-1]+1
    bank['name'].append(name)
    bank['bal'].append(bal)
    bank['acc'].append(acc)
    bank['password'].append(password)
    update()
    print("\n your account sucessfully created")
    print("\nNote down your account number:{}".format(acc))
    main()

    
def main():
    print("Welcome to bank program".center(300,"*"))
    print("Menu")
    print("|n\n1.login\n2.signup\n3.exit\n\n")
    ch=int(input("enter your choise:"))
    print("processing".center(300,"*"))
    time.sleep(2)
    if ch == 1:
        login()

    if ch ==2:
       signup()

    elif ch== 3:
       exit(0)

    else:
       print("\n\ninvalid input\n try Again")
       main()

        
        
if __name__ =="__main__":
    main()
