salary=int(input("Salary:"))
age=int(input("age:"))
if (salary>=20000 or age<=25):
    print("You condition is satisfied \nEnter Your loan amount")
    loan=int(input())
    if(loan<=50000):
        print("You are eligible for loan")
    else:
        print("Maximum loan amount is 50000")
else:
    print("Not eligible for loan")
