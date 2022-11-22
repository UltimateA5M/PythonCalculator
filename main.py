# Function Definitions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y
    
def divide(x, y):
    return x / y

# UI
print("Operations:")
print("1 = Add")
print("2 = Subtract")
print("3 = Multiply")
print("4 = Divide")

ops = ['1','2','3','4']
condition = True
while condition:
    # take user input
    op = input("Choose operation (1,2,3,4):")
        
    if op in ops:
        num1 = float(input("Enter 1st number: "))
        num2 = float(input("Enter 2nd number: "))
        
        if op == '1':
            print(num1, '+', num2, '=', add(num1, num2))

        elif op == '2':
            print(num1, '-', num2, '=', subtract(num1, num2))

        elif op == '3':
            print(num1, '*', num2, '=', multiply(num1, num2))

        elif op == '4':
            print(num1, '/', num2, '=', divide(num1, num2))
        
        # check if user wants another calculation
        # break the while loop if answer is no
        continueCalc = input("Do you want to perform another calculation? (y/n): ")
        if continueCalc == 'n':
            print("Quitting..")
            break
    else:
        print("Invalid Input")
    