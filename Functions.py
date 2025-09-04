##Write a functions code to perform add,sub,multi and divide using function
##def add():
##    a=int(input("Enter a:"))
##    b=int(input("Enter b:"))
##    print(a+b)
##def sub():
##    a=int(input("Enter a:"))
##    b=int(input("Enter b:"))
##    print(a-b)
##def multi():
##    a=int(input("Enter a:"))
##    b=int(input("Enter b:"))
##    print(a*b)
##def divide():
##    a=int(input("Enter a:"))
##    b=int(input("Enter b:" ))
##    print(a/b)
##    
##n=input("Enter the Operations:")
##if(n=="add"):
##    add()
##elif(n=="sub"):
##    sub()
##elif(n=="multi"):
##    multi()
##elif(n=="divide"):
##    divide()

##Basic functions call    
##def find():
##    print("The functions is done when its call , till then it doesnot perform")
##find()

##Variable and Value stored in functions
##def find():
##    print("The function shouldn't call first",a)
##find(10)   #This 10 value is stored in a

##Asking value from the user and perform even or odd functions
##def find(a):
##    if(a%2==0):
##        print("Its an even number")
##    else:
##        print("Its an odd number")
##a=int(input("Enter the value a:"))
##find(a)

##Input a,b from the user as its range to print number within its range
##def find(a,b):
##    for i in range(a,b):
##        print(i)
##a=int(input("Enter a:"))
##b=int(input("Enter b:"))
##find(a,b)

##Print the from range 10 to 20 in reverse order using while loop
##def find(a):
##    while(a>10):
##        print(a)
##        a=a-1
##a=int(input("Enter a:"))
##find(a)
        
##Using a consturctor functions and keyword
##class laptop():
##    def __intit__(self):
##        self.ram=""
##        self.processor=""
##    def desgin(self):
##        print("The ram design is cool...",self.ram)
##hp=laptop()
##dell=laptop()
##hp.ram=input()
##hp.processor=input()
##dell.ram="5gb"
##dell.processor="i7"
##hp.desgin()
##dell.desgin()

##Create a class called student and create a variable=name and reg number using constructor
##Create a funcction called display which should display name and reg of the student.
##class student():
##    name=""
##    register=""
##    def display(self):
##        print("The name is",self.name)
##        print("The reg is",self.register)
##stu=student()
##stu.name=input()
##stu.register=input()
##stu.display()

##Create a class called fruit and create variable olor using __init__ method.
##Create a object called apple and pass the color variable
##class fruit():
##    def __init__(self,col):
##        self.color="black" 
##        print("The color is:",self.color)
##apple=fruit()
##print(apple.color)

##Create a class called teacher.Create a variable=name,reg no using constructor.
##Create a function called display which should display a name and reg no of
##the teacher.
##Create ti and t2 object and pass the name and reg no value through object.
class teacher():
    def __init__(self,a,b):
        self.name=a
        self.reg=b
    def display(self):
        print("The name is",self.name)
        print("The reg is",self.reg)
t1=teacher("yashu","421")
t2=teacher("bankai","422")
t1.display()

