##Inheritence - Using of multiple class and use one data class to other class
##Basic functions :-
##class dad():
##    def phone(self):
##        print("Dad is calling")
##class son():
##    def sphone(self):
##        print("Son is calling")
##y=son()
##y.sphone()

##Single inheritence - Class using other class
##class dad():
##    def phone(self):
##        print("Dad is calling")
##class son(dad):
##    def sphone(self):
##        print("Son is calling")
##y=son()
##y.phone()

##Multiple Inheritance - Class using multiple other class
##class dad():
##    def phone(self):
##        print("Dad is calling")
##class son():
##    def sphone(self):
##        print("Son is calling")
##class grandson(dad,son):
##    def message(self):
##        print("No phone.......")
##y=grandson()
##y.phone()
##y.sphone()

##Multi-level inheritence - Class using by another class by class
##class dad():
##    def phone(self):
##        print("Dad is calling")
##class son(dad):
##    def sphone(self):
##        print("Son is calling")
##class grandson(son):
##    def message(self):
##        print("No phone.......")
##y=grandson()
##y.phone ()

##Hierarchical Inheritance - Single Class is used by two or more class
##class dad():
##    def phone(self):
##        print("Dad is calling")
##class son(dad):
##    def sphone(self):
##        print("Son is calling")
##class grandson(dad):
##    def message(self):
##        print("No phone.......")
##y=grandson()
##y.phone ()

##Hybrid Inheritance - Combinations uses of all types of inheritance
##class father():
##    def birth(self):
##        print("I have two son")
##class son1(father):
##    def king1(self):
##        print("I am son1 king")
##class son2(father):
##    def supportingking(self):
##        print("Supporting king og kings")
##class kingdom(son1,son2):
##    def rule(self):
##        print("A generations of ruling king")
##life=kingdom()
##life.king1()
##life.birth()

##Same functions used for different operations is called polymorphism.
##def add(a,b,c=0):
##     print(a+b+c)
##add(1,2)
##add(1,2,3)

##Method Over-ridding a functions
##class animal():
##     def sound(self):
##          print("Dogs")
##class dog(animal):
##     def sound(Self):
##          print("cat")
##y=dog()
##y.sound()

##Create a base class called shape with a method area() that return 0.
##Create a derived class called rectangle that inherits from shape and overrides the  area
##method to calculate and return the area of the rectangle.
##class shape():
##    def area(self):
##        return 0
##class rectangle(shape):
##    def area(self,a,b):
##        self.a=a
##        self.b=b
##        print("Area of the rectangle is:",a*b)
##a=rectangle()
##a.area(10,20)

##Create a base class called person with a constructor that takes a name as a parameter.
##Create a derived class called student that inherit from person and has a constructor that
##takes a parameter called grade.Write a method in student to display name and grade.
##class person():
##    def __init__(self,a):
##        self.name=a
##class student(person):
##    def __init__(self,a,grade):
##        super().__init__(a)
##        self.b=grade
##    def display(self):
##        print(self.name,self.b)
##s=student("Yashu",99)
##s.display()

##Create a base class called vehicle with a method start() that print"Vehicle start".
##Create a derived class called car that inherits from vehcile and overrides that start()
##method to print("Car started")
##class vehicle():
##    def start(self):
##        print("Vehicle started")
##class car(vehicle):
##    def start(self):
##        print("Car started")
##z=car()
##z.start()

##Create a base class called employee with properties name and salary.
##Create  a derived class called manager that inherits from employee and adds department.
##Write a method in manager to display name,salary and department of the manager.
##class employee():
##    def __init__(self,a,b):
##        self.name=a
##        self.salary=b
##class manager(employee):
##    def __init__(self,a,b,c):  #Write all the input variable 
##        super().__init__(a,b)  #Write input variable of inherit class
##        self.department=c
##    def display(self):
##        print(self.name,self.salary,self.department)
##z=manager("fsfd","dfsd","sds")
##z.display()

    
    
