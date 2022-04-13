class Atm :
    def __init__(self,cardNumber,pin):
        self.cardNumber = cardNumber
        self.pin = pin 

    def check_balance (self):
        print("Your balance is 10")

    def withdrawal (self,amount):
        new_amount = 10 - amount
        print("amount withdrawn" + str(amount) + "and your remaining balance is :" + str(new_amount))

def main():
    card_number = input("Insert your card number :")
    pin_number = input("Enter your pin number :")

    new_user = Atm(card_number, pin_number)
    print("Chose your activity")
    print("1.Balance enquity 2.Withdrawal")

    activity = int(input("Enter the activity number"))

    if (activity == 1):
        new_user.check_balance()
    elif(activity == 2):
        amount = int(input("enter the amount:"))
        new_user.withdrawal(amount)
    else:
        print("enter a valid number ")
if __name__ == "__main__" :    
    main()




      