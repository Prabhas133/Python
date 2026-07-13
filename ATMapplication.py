#Project
#ATM application
while True:
    Account = 1000000
    card = "c"
    pwd = 2004
    print("\n")
    c = input("Insert the card : ")
    if c == card:
        print("Welcome Prabhas")
        p = int(input("Enter the password : "))
        if p == pwd:
            Account = 100000
            choice = int(input('''Choose the option
                                        1.Balance
                                        2.Withdraw : '''))
            if choice == 1:
                print("Your Balance is : ",Account)
            elif choice == 2 :
                withdraw = int(input("Enter the withdraw amount : "))
                if withdraw <= Account:
                    balance = Account - withdraw
                    print("Collect your cash")
                    print("Remaining balance : " ,balance)
                else:
                    print("Insuffficent balance")
            else:
                print("Invalid option")
        else:
            print("Invaild password")
    else:
        print("Invalid card")


        
        
        

