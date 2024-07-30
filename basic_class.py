class Customer():
    def __init__(self, name, mship):
        self.name = name
        self.mship = mship
    
    # comment this and see how we have overrideen str method
    def __str__(self):
        return self.name+" "+self.mship
    
    @staticmethod
    def check():
        return "A static method which used for class in general not for an particular customer"
    
    def update_mpship(self, new_mship):
        self.mship = new_mship

    def print_cus(lis):
        for i in lis:
            print(i)
        print([i for i in lis])
    
    __repr__ = __str__ # this make sure we print content rather than memory location, comment it and see its effect on print(a)

a = Customer("sasi","gold")
b = Customer("lassi", "diamond")

print(a, b)

lisa = [a,b]

a.update_mpship("iridum")
print(a)

print(a.check()) # if you dont put @static method , this will give error

#Customer.check() # DOESN"T GIVE ERROR
#Customer.print_cus(lisa)