import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
# Generate password
def generatePassword():
    passwordLength = int(input("Enter the length of your password: "))
    print("")

    random.shuffle(characters)

    password = []
    
    for x in range(0, passwordLength):
        password.append(random.choice(characters))
    
    random.shuffle(password)

    password = "".join(password)

# print password
    print(password+"\n")
# if initial response is no, exit program

# ask the user if they want to generate a password or not
option = input("Do you want to generate the password? (Yes/No): ")
print("")
# if yes, ask for the password length
if option == "Yes":
    generatePassword()
elif option == "No":
    print("Program ended.")
    quit()
else:
    print("Invalid input.")