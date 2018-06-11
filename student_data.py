student ={
        "name":["stuti","chotu","runjhun","shalu"],
        "address":["123asd","145ert","567huy","987gty"],
        "coures":["python","java","c","php","swift"],
        "roll_no":[1,2,3,4]
        }
while input("enter ant think to countinue"):
    print('\n\n1.login\n2.signup\n\n')
    ch=int(input("enter your choise"))
    if ch == 1:
       name=input("enter your name")
       roll_no=int(input("enter your rollno"))
       if roll_no in student['roll_no']:
          i=student['roll_no'].index(roll_no)
          if name==student["name"][i]:
             print("******processing*****")
             print("\n\n1.update\n2.delete\n3.view\n\n")
             ch=int(input("enter your choise"))
             if ch == 1:
                roll_no=int(input("enter your roll_no"))
                if roll_no in student['roll_no']:
                   i=student["roll_no"].index(roll_no)
                   student['name'][i]=="alka"
                   #student.update((student['name'][i],"alka"))
                   print(student)
                else:
                   print("no student")
             elif ch == 2:
                roll_no=int(input("enter your roll_no"))
                if roll_no in student ["roll_no"]:
                    i=student["roll_no"].index(roll_no)
                    k=student['name'].remove(student["name"][i])
                    l=student['address'].remove(student["address"][i])
                    m=student['coures'].remove(student["coures"][i])
                    n=student["roll_no"].remove(student["roll_no"][i])
             elif ch == 3:
                
                  roll_no=int(input("enter your roll_no"))
                  if roll_no in student['roll_no']:
                     i= student['roll_no'].index(roll_no)
                     print(student['name'][i])
                     print(student['address'][i])
                     print(student['coures'][i])
                  else:
                    print("\n no such student\n")
                    print("\nYou can signup to studentdata")
            
             else:
               print("Invalid choise")




    elif ch == 2:
          name = input("\n\n Enter your Name:")
          coures=input("\n\n enter your coures:")
          address=input("\n\n enter your address:")
          roll_no=student['roll_no'][-1]+1
          student['name'].append(name)
          student['coures'].append(coures)
          student['address'].append(address)
          student['roll_no'].append(roll_no)
          print("\n student is added sucessfully")
          print("\n your roll_no :{}".format(roll_no))
    else:
        print("invalid choice")


