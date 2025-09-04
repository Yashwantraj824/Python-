##Create a class and ask input from the user and print its functions
##class goa():
##    name=""
##    date=""
##    def party(self):   
##        print("Let's party........")
##    def beach():
##        print("Let's enjoy the beach view")
##
##
##yash=goa()   #Object ,Using a class with an object
##yash.name=input()  #inputing a data in the class
##yash.party() #Calling a functions in the class using object

##Print only the a particular objects name 
##class goa():
##    name=""
##    date=""
##    def party(self):   
##        print("Let's party........")
##    def beach():
##        print("Let's enjoy the beach view")
##
##
##yash=goa()
##yash.name=input()
##yas.name=input()
##print("Name:",yash.name)

##Write a class called laptop and create a following variables and functions
##class laptop():
##        price=""
##        processor=""
##        Ram=""       
##hp=laptop()
##dell=laptop()
##lenovo=laptop()
##
##hp.price=int(input("Enter price:"))
##hp.processor=input("Enter the procssor:")
##hp.ram=input("Enter space:")
##
##print(hp.price,hp.processor,hp.ram)

##Craete a class and have or use a common class variable and print
##class yashu():
##    name="Yashu"
##    def __init__(self,a,b):
##        self.section=a
##        self.reg=b
##    def display(self):
##        print("Reg no:",self.reg)
##        print("Name:",self.name)
##        print("Sections:",self.section)
##y=yashu("er","42")
##y.display()

##Call a function and using a class variable using @classmethod
class laptop():
    ct="c-type"
    def __init__(self):
        self.brand=""
        self.price= 34 
    def sp(self,price):
        self.price=price
    def gp(self):
        print(self.price)
    @classmethod
    def cct(cls):
        cls.ct="b-type"
        print("Change type........")
    @staticmethod
    def pri():
        print("gopal")

hp=laptop()
hp.gp()
laptop.pri()
laptop.cct()

