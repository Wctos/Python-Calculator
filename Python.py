print("\___||__'_'__||___/ - This Tool Made By Wctos")

def addition():
    Fn = float(input(' > Enter The First Number: '))
    Sn = float(input(' > Enter The Second Number: '))
    Result = Fn + Sn
    print(" > The Result is:", Result)

def subtraction():
    Fn = float(input(' > Enter The First Number: '))
    Sn = float(input(' > Enter The Second Number: '))
    Result = Fn - Sn
    print(" > The Result is:", Result)

def multiplication():
    Fn = float(input(' > Enter The First Number: '))
    Sn = float(input(' > Enter The Second Number: '))
    Result = Fn * Sn
    print(" > The Result is:", Result)

def divide():
    Fn = float(input(' > Enter The First Number: '))
    Sn = float(input(' > Enter The Second Number: '))
    if Sn == 0:
        print(" > Error: Division by zero")
    else:
        Result = Fn / Sn
        print(" > The Result is:", Result)

print(" > Enter 'Addition' to add numbers")
print(" > Enter 'Subtraction' to subtract numbers")
print(" > Enter 'Multiplication' to multiply numbers")
print(" > Enter 'Divide' to divide numbers")

Calculator = input(" > What operation do you want to perform? : ")

if Calculator == 'Addition':
    addition()
    
elif Calculator == 'Subtraction':
    subtraction()

elif Calculator == 'Multiplication':
    multiplication()

elif Calculator == 'Divide':
    divide()

else:
    print(" > Error: Wrong input")
