##Types of Error :-

##Complier error-Error while complie
##print("sda")
##pirnt("fds")  #Synatx/call error

##Logical error-Logical mistake
##a=10
##b=20
##print(a+a)  #Logical error in code

##Runtime error - Error when the code run and ask for an input.
##a=int(input())
##b=int(input())  #ValueError pop() if wrong datatype is inputed
##print(a+b)

##Exceptions Handling :-
##try and exceptions - Used if without any conditions and try out.
##If its correct it print or goes to next methods.And exceptions as e where e
##show use what error has comitted in the program
##try:
##    a=int(input())
##    b=int(input())
##    print(a+b)
##except Exception as e:
##    print("Give an integer value for both",e)

##This Exceptions can be only directed to one type of error by replacing exceptions to
##ValueError,NameError,SyntaxError and give different workflow.
##
##try:
##    a=int(input())
##    b=int(input())
##    c=input()
##    print(a+b)
##    print(c/a)
##    printh(a*b)
##except TypeError as e:
##    print("Logical mistake da",e)
##except ValueError as e:
##    print("Enter a datypes correctly",e)
##except NameError as e:
##    print("Syntax error buddy",e)
##except Exception as e:
##    print("Error da.....",e)

##finally() used to print after what ever happened before
##
##try:
##    a=int(input())
##    b=int(input())
##    print(a+b)
##except Exception as e:
##    print("Give an integer value for both",e)
##finally:
##    print("Good job")
