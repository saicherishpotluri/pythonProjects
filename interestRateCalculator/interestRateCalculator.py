# collect the necessary inputs: principal, apr, years
def main():
    print(" This is a montly payment loan calculator ")
    print("")

    principal = float(input("Enter the loan amount: "))
    apr = float(input("Enter the annual interest rate: "))
    years = int(input("Enter the number of years: "))
# calculate the monthly payment
    monthlyInterestRate = apr / 1200
    months = years * 12
    monthlyPayment = principal * monthlyInterestRate / (1 - (1 + monthlyInterestRate) ** (-months))
# show to the user
    print(" The monthly payment for this loan is: %.2f" % monthlyPayment)

main()