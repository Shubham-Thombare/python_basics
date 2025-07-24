# Banking Program

def show_balance(balance):
    print(f"Your balance is ${balance:.2f}")

def deposit():
    print("****************************")
    amount = float(input("Enter the amount to be deposited: "))
    print("****************************")

    if amount < 0:
        print("****************************")
        print("That is not a valid amount")
        print("****************************")

    else:
        return amount    
    
def withdraw(balance):
    print("****************************")
    amount = float(input("Enter the amount to withdrawn: "))
    print("****************************")

    if amount > balance:
        print("Insufficient Balance")
        return 0 
    elif amount < 0:
        print("Amount must be greater than 0")
        return 0 
    else:
        return amount
            
def main():
    balance = 0 
    is_running = True

    while is_running:
      print("****************************")
      print("   BANKING PROGRAM   ")
      print("1.Show balance")
      print("2.Deposit")
      print("3.Withdrawl")
      print("4.Exit")
      print("****************************")

      choice = input("Enter your choice(1-4): ")

      if choice == '1':
         show_balance(balance)
      elif choice == '2':
        balance += deposit()   
      elif choice == '3':
        balance -= withdraw(balance)
      elif choice == '4':
        is_running = False
      else:   
        print("****************************")
        print("That is not a valid choice")     
        print("****************************")

    print("****************************")
    print("Thank You! Have a Nice Day! ")
    print("****************************")

if __name__ == '__main__':
    main()
