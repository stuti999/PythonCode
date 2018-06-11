def addtag(*tags):
    def dec(func):
        def mk(s):
            k=func(s)
            for tag in tags:
                k="<{0}>{1}</{0}>".format(tag,k)
            return k
        return mk
    return dec

@addtag('b','p','div')
def new(s):
     pass
 
s=input("type someting:\n\n")
r=new(s)
print(r)
