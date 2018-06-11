import json
bank = {
        'name':['stuti','anuj','senthil','arvind'],
        'bal':[10000,20000,30000.40000],
        'acc':[1001,1002,1003,1004],
        'password':['abc','xyz','python','redhat']
        }
fp=open("bank.db","w")
json.dump(bank,fb)
fp.close()
