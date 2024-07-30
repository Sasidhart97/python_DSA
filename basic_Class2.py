class Student():

    school = "Tata"
    def __init__(self, m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.lap = self.Laptop()
    
    # instance method
    def calc_avg(self):
        return (self.m1+self.m2+self.m3)/3
    
    # instance 
    @classmethod
    def schoolName(cls):
        return cls.school
    
    @staticmethod
    def info():
        return "This is a student class in learning module"
    
    class Laptop:

        def __init__(self):
            self.brand = "HP"
            self.chip = "i8"
        
        def show(self):
            return self.brand, self.chip

class Boy(Student):

    def gender(self):
        self.gender = "male"
        return self.gender

a = Student(20,21,22)
b = Student(30,31,32)

print(a.calc_avg())

print(Student.school, a.school, b.school, a.schoolName())
print(a.info(), b.info(), Student.info())

print(id(a), id(b))

print(a.lap.show())

# print(Student.Laptop.show()) - gives error below one will work
lap1 = Student.Laptop()
lap1.show()

c1 = Boy(1,2,3)
print(c1.gender(), c1.calc_avg(), c1.lap.show())