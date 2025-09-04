Python - Pandas - Numpy - MySQL 

1.Print its data type

  -a=10
  print(type(a)) #<class'int'>

2.Casting - converting datatype to another datatype

  -a="10"  #A is in string format , cannot perform maths operations
  print(int(a)) or a=int("10")  #Converted in int format

3.Default variable are considered as Strings when asking input

  -a=input()
  If only int datatype needed perform
  -a=int(input())  #If at all char used , it doesnot accept it

4.Conditions Statement:
    
  -IF statement:
      if condition:
          statement

  -IF and Else:
      if conitions:
          statement
      else:
          statement
    Note: Its not need madortary to have else a condition . 
          
  -IF and If conditions:
      if conditions:
          statement
      if conditions:
          statement
    Note: It will check all the condition even as satisfied with pervious one .
    Due to which it increase in time complexitiy.
    
  -IF and ELIF conditions:
      if conditions:
          statement
      elif conditions:
          statement
      else conditions:
          statement
    Note: Once it satisfied with the condition ,it wonot check next.

   -Nested IF:
       if condition:
           if conditions:
               if condition:
                   statement
                else:
           else:
       else:
    Note:Performed when a conditions is true and to check another conditions
    upon conditions with its else.

5.Looping Statement:
    
    -For Loop:
        for <Variable> in statement<range,list.etc>:
    Note:Performed when the no of iterations are known
        
    -While Loop:
        while(conditions):
    Note:Performed when the no of iterations are unknown.Can perform infinite
    if not check the statement conditions properly.

    -Nested loop:
        for i in range(1,5):
            print()
            for j in range(1,i+1):
                print(j,end="")
    Note:Loop used inside and another loop.Most used in pattern sloving questions

6.Collections or Data Structure:
    
    -List[a,b]  Ordered,changeable and allow duplicate members.Add and Remove possible
    
    -Tuple(a,b) Ordered,unchangeable and allow duplicate members.Add and remove not possible
    
    -Set{a,b} Unordered,unchangable but no duplicate members.Add and remove possible

    -Dictionary{"":"","":""} Ordered,changeable but no duplicate members.

7.List[] and Tuples() Operations-
  input: a=[10,20,30]
  
  -a.append(40)   #Add an element
   a=[10,20,30,40]  

  -a.extend([40]) #Add element on an fix list
   a=[10,20,30,40]

   a.extend([b]) #a=[1,2] and b=[3,4] Join two list
   a=[1,2,3,4]
   
  -a.insert(2,40) #Add element in a specific locations
   a=[10,20,40,30]

  -print(a.count(20))    #Count no of same duplicate member
   1

  -print(a.clear())      #Empty the list
   []

  -print(a.index(40))    #Tells the positions of the element mentioned
   3

  -a.remove(40)   #Remove the specific element in the list
   a=[10,20,30]

  -a.pop(2) or a.pop()#Remove element in an specific positions or it remove last element
   a=[10,20]

  -a.reverse()    #Reverse the ordered
   a=[20,10]

  -a.sort()       #Arrange in increase order of value
   a=[10,20]

8.String Operations-

  -a.capitalize()  #Arrange in capitalize manner
  
  -a.lower()   #Arrange in lower case
  
  -a.upper()   #Arrange in upper case
  
  -a.count(l)  #Count no of char mentioned in the string
  
  -a.index(o)  #Mention the positions of the char
  
  -a.find(o)   #Find the char anf tells its positions in the string

  -a.replace('/','-')   #Replace a char with another char

  -a.split('/')# Split based on the specific char in the string

9.Set{} Operations-
  a={1,2,3} and b={3,4,5}

  -print(a|b)  #Union the set
   {1,2,3,4,5}

  -print(a&b)  #Intersections or print common elements in sets
   {3}

  -print(a-b)  #Difference or uncommon element in a compared to b
   {1,2}

  -print(a^b)  #Symmetric or print all uncommon element
   {1,2,4,5}

  -a.add(4)    #Add element in the set
   {1,2,3,4}

  -a.remove(4)  #Remove the specific element in the set
   {1,2,3}

  -a.pop()   #Remove first element
   {2,3}

10.Dictionary Operations{"":""}-
  a={"a":"b","c":"d"}

  -print(a) # Print all a

  -print(a["a"])   #Print the value of a
   b

  -print(a.keys()) #Print all key
   dict_keys({'a','c'})

  -print(a.values())#Print all values
   dict_values({'b','d'})

  -a["e"]="f"    #Add in dictionary
   print(a)
   {"a":"b","c":"d","e":"f"}
   
  -a.update({"e":g})    #Update in dictionary
   print(a)
   {"a":"b","c":"d","e":"g"}
   
  -a.pop(e)   #Remove in dictionary
   print(a)
   {"a":"b","c":"d"}

  -del a  #Delete a Complete dictionary

  -a.clear() #Clear data in the dictionary
   {}

11.Functions -

  -Basic functions call:
      def find():
          print("The functions is done when its call , till then it doesnot perform")
      find()
  Note:The functions is done when its call , till then it doesnot perform
  The function shoulnot call first.

  -Variable and store:
      def find(a):
          print("The function shouldn't call first",a)
      find(10)   #This 10 value is stored in a
   Note:If a variable is method in the def,then it should be assigned a value even in use
   or not.if value is given and not variable is method it show error and wise-visa.

   -Variable is asked from the user and performed in the functions:
       def find(a):
           ...........
       a=int(input())
       find(a)  #The value a is stored and only is pass in the functions 
      
12.Class and Object -

  -Class an contain n number of functions and variable.

  -To works with class create a object and assign it(object=class())

  -To insert a data in the variable in the class.Type object.variable=""

  -To call a functions in the class.Type object.functions_name

  -Can contains n number of data with same configaration in an class and
   call it with the help of objects of the data. 

13.Constructor and keyword:
    
  -Def __init__(self) :-Using this keyword functions it will automatically runs
     when the class is called .(Normally we have to call the functions in an class).

  -Instance variable :-A variable that changes time to time in an code.(self)

  -Class variable :-A variable that is common in the class and be used in all functions.
14. Methods:

  - Functions are called methods in languages.

  -CLASS METHOD:
    Use to call a function by its class name and using class varible.
    Use a syntax before @classmethod.

  -STATICMETHOD:
    Use to call a function by its class name and print its which have none operations but
    just a multiple print functions .Use  a syntax before as @staticmethod

15.Inheritence - Using of multiple class and use one data class to other class

  -Single inheritence-Using a class data(function or method) and call by the another class.
    EX-
      class parentclass():
          ..................
      class son(parentclass):
          .................
       y=son()
       y.phone() #call a function in the parentclass
  -Multi-level inheritence -Using  a class data/function by class to class
   EX-
     class parentclass():
          ..................
    class son(parentclass):
          .................
    class grandson(son):
          ................
    y=son()
    y.phone() #call a function in the parentclass

  -Multiple inheritance-Using a class data by other classes

    class parentclass():
          ..................
    class son():
          .................
    class grandson(parentclass,son):
          ................
    y=son()
    y.phone() #call a function in the parentclass

  -Hierarchical Inheritance - Single class is used by two or more class
   
    class parentclass():
          ..................
    class son(parentclass):
          .................
    class grandson(parentclass):
          ................
    y=son()
    y.phone() #call a function in the parentclass

  -Hybrid Inheritance - Combinations uses of all types of inheritance .

    class father():
          ....................
    class parentclass(father):
          ..................
    class son(father):
          .................
    class grandson(parentclass,son):
          ................
    y=son()
    y.phone() #call a function in the parentclass

16.Super() - Its used to call a constructor from its inherits class with
   its own constructor to input data and functions it.
   
  class employee():
    def __init__(self,a,b):
        self.name=a
        self.salary=b
  class manager(employee):
    def __init__(self,a,b,c):  #Write all the input variable 
        super().__init__(a,b)  #Write input variable of inherit class
        self.department=c
    def display(self):
        print(self.name,self.salary,self.department)
  z=manager("fsfd","dfsd","sds")
  z.display()

17.Encapsulation - A private variable and method that can be used within a class
   It uses acces modifier to different use cases.

  -Public: Accessible from anywhere. No underscore prefix.(Normal code)

  -Protected:Intended for internal use within the class and its subclasses.
    Indicated by a single underscore (_variable).(Inheritance usecases)
    Can be called outside the class

  -Private: Strictly internal to the class.
    Indicated by a double underscore (__variable),which triggers name mangling.
    Canot call oustside the class.
   
18.Exception Handling - Type of Error

  -Complie time error- Error pop when it complie by the line-by-line.
    Mostly an syntax/call function error(NameError).

  -Logical error - Error with logical operations

  -Runtime error- Error pop when the program runs.(ValueError)
   Like the program ask for int value but passing an string.

  Types of Exceptions Handling -

  Exceptions Handling :-
  - try and exceptions - Used if without any conditions and try out.
    If its correct it print or goes to next methods.And exceptions as e where e
    show use what error has comitted in the program

    try:
        a=int(input())
        b=int(input())
        print(a+b)
    except Exception as e:
        print("Give an integer value for both",e)

   -This Exceptions can be only directed to one type of error by
    replacing exceptions to ValueError,NameError,SyntaxError
    and give different workflow.

    

