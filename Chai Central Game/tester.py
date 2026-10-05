import random
class alass(object):
    def __init__(self):
        self.tea = ["assam", "masala", "badshah", "royal", "tulsi", "darjeeling", "kashmiri"]
        #self.variable = [assam, masala, badshah, royal, tulsi, darjeeling, kashmiri]
        self.number = [0,1,2,3,4,5,6]
    def typeoftea(self, string):
        random.shuffle(self.number)
        self.a = self.number.pop()
        self.b = self.number.pop()
        self.one = self.tea[self.a]
        self.two = self.tea[self.b]
        variable_name = self.one + self.two
        return variable_name
    
a = alass()
x = a.typeoftea()
