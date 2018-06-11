class Grass:
    Institute_Name ="Grass Solution Private LTD"
    trainers={
            "Linux":['rajat','Gaurav','Naveen'],
            "python":["sachin"]
            }

    def __init__(self,st_name,st_fees,st_course):
        self.name=st_name
        self.fee=st_fees
        self.course=st_course
        self.trainer=random.choice(Grass.Trainer[st_course])
        def show(self):
            print("student name:",self.name)
            print("student fee:",self.fee)
            print("student course:",self.course)
            print("student trainer:",self.trainer)
             
