
def main():
    print("Welcome to email slicer")
    print("")
    #collect email from user
    emailInput = input("Enter email address:")
    #split the email using delimiter '@', the first part as user name,and second name as domai
    (userName,domain) = emailInput.split("@")
    #split domain using delimiter '.'
    (domain, extension) = domain.split(".")
    print("Username: ", userName)
    print("Domain: ", domain)
    print("Extension: ", extension)

main()