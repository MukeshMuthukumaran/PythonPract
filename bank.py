def bank_system():
    balance = 0
    
    while True:
        print("1. Deposit")
        print("2. Withdraw")
        print("3. View Balance")
        print("4. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            amount = int(input("Enter the amount to deposit: "))
            balance += amount
            print(f"Rs{amount} deposited. New balance: Rs{balance}")
        
        elif choice == 2:
            amount = int(input("Enter the amount to withdraw: "))
            if amount > balance:
                print("Insufficient balance")
            else:
                balance -= amount
                print(f"Rs{amount} withdrawn. New balance: Rs{balance}")
        
        elif choice == 3:
            print(f"Current balance: Rs{balance}")
        
        elif choice == 4:
            print("Exiting the system...")
            break
        
        else:
            print("Invalid choice. Please try again.")


bank_system()
