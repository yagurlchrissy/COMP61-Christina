def atm_simulator():
    balance = 1000.0  # Initial balance
    
    print("Welcome to Simple ATM Simulator!")
    
    while True:
        print("\nMenu:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 4.")
            continue
        
        if choice == 1:
            print(f"Your current balance is: ${balance:.2f}")
        
        elif choice == 2:
            try:
                amount = float(input("Enter the amount to deposit: "))
                if amount <= 0:
                    print("Invalid deposit amount. Please enter a positive number.")
                else:
                    balance += amount
                    print(f"Deposit successful! Your new balance is: ${balance:.2f}")
            except ValueError:
                print("Invalid input! Please enter a valid amount.")
        
        elif choice == 3:
            try:
                amount = float(input("Enter the amount to withdraw: "))
                if amount <= 0:
                    print("Invalid withdrawal amount. Please enter a positive number.")
                elif amount > balance:
                    print("Insufficient funds.")
                else:
                    balance -= amount
                    print(f"Withdrawal successful! Your new balance is: ${balance:.2f}")
            except ValueError:
                print("Invalid input! Please enter a valid amount.")
        
        elif choice == 4:
            print("Thank you for using the ATM. Goodbye!")
            break
        
        else:
            print("Invalid choice! Please enter a number between 1 and 4.")

# Run the ATM simulator
atm_simulator()
