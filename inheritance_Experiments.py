class A():
    def __init__(self, m):
        self.m = m
        print ("A init")
    
    def f1(self):
        print("f1 feature", self.m)
    
    def f2(self):
        print("f2 feature", self.m)
    
class B(A):

    def __init__(self,m):
        super().__init__(m)
        print("B init")

    def f3(self):
        print("f3 feature")

class C(B):
    def __init__(self,m):
        super().__init__(m)

    def f4(self):
        print("f4 feature")

a = C(3)
a.f1()