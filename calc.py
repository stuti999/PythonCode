def calc(x,y,z):
     if z=="+":
         return x+y
     elif z=="-":
         return x-y
     elif z=="*":
         return x*y
     elif z=="%":
         return x%y
     elif z=="//":
         return x//y
     elif z=="**":
         return x**y
     elif z=="/":
         if y:
             return x/y
         else:
             return "error"
     else:
         print("invalid choise")
while input("\n\npress any key"):
    x=int(input("x:"))
    y=int(input("y:"))
    z=input("choice (+,-,/,%,//,**,/)")
calc(x,y,z)    
