# define the functions needed: add, sub, mul, div
def add(num1, num2):
    result = num1 + num2
    print(str(num1)+" + "+str(num2)+" = "+str(result) + "\n")


def sub(num1, num2):
    result = num1 - num2
    print(str(num1)+" - "+str(num2)+" = "+str(result) + "\n")


def mul(num1, num2):
    result = num1 * num2
    print(str(num1)+" * "+str(num2)+" = "+str(result) + "\n")


def div(num1, num2):
    result = num1 / num2
    print(str(num1)+" / "+str(num2)+" = "+str(result) + "\n")


# while loop to continue untill user wants to exit
while True:
    # print options to the user
    print("A. Addition\nB. Subtraction\nC. Multiplication\nD. Division\nE. Exit")
    # ask for values
    choice = input("Enter your choice:")

    if choice == "a" or choice == "A":
        print("Addition")
        num1 = int(input("Enter first number:"))
        num2 = int(input("Enter first number:"))
        # call the functions
        add(num1, num2)
    elif choice == "b" or choice == "B":
        print("Subtraction")
        num1 = int(input("Enter first number:"))
        num2 = int(input("Enter first number:"))
        # call the functions
        sub(num1, num2)
    elif choice == "c" or choice == "C":
        print("Multiplication")
        num1 = int(input("Enter first number:"))
        num2 = int(input("Enter first number:"))
        # call the functions
        mul(num1, num2)
    elif choice == "d" or choice == "D":
        print("Division")
        num1 = int(input("Enter first number:"))
        num2 = int(input("Enter first number:"))
        # call the functions
        div(num1, num2)
    elif choice == "e" or choice == "E":
        print("Program ended")
        quit()
