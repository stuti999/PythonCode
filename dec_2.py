def dec(old_fun):
    def make_up(x,y):
        print("value of x=:",x)
        print("value of y=",y)
        print("result=",x+y)
        print("thanks")
    return make_up
@dec
def new(x,y):
    pass 
new(3,4)

