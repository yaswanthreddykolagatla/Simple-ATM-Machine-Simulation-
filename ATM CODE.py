def atm_simulator():
    balance = 1000  # Initial balance
    pin = 1234      # Example PIN for the ATM
    max_attempts = 3 
    attempts = 0 
                                        # Ask for the user PIN
    while attempts < max_attempts:
        try:
            user_pin = int(input("Please enter your 4-digit PIN: "))
        except ValueError:
            print("Invalid PIN. Access Denied.")
            continue
        
        # Check if the PIN is correct
        if user_pin == pin:
            print("Welcome to the ATM!")
            break
        else:
            attempts +=1
            print(f"Please enter valid pin. You have {max_attempts-attempts} attempts left")
    else:
        print("You have reached your maximum attempts in a day")
        return                           
                                        # ATM operation loop
    while True:
        print("Choose an option:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        option = input("Enter your choice: ")

        if option == '1':
            print(f"Your current balance is: {balance:.2f}")
            
            
        elif option == '2':
            deposit = int(input("Enter amount to deposit: $"))
            if deposit > 0:
                balance += deposit
                print(f"Deposited amount is: ${deposit:.2f} \nCurrent balance is: ${balance:.2f}")
            else:
                print("Invalid deposit amount.")
        
        elif option == '3':
            withdraw = int(input("Enter amount to withdraw: $"))
            if withdraw > balance:
                print("Insufficient balance.")
                print(f"Current balace is:{balance:.2f}")
            elif withdraw > 0:
                balance -= withdraw
                print(f"${withdraw:.2f} has been withdrawn. \nCurrent balance is: ${balance:.2f}")
        
        elif option == '4':
            print("Thank you for using ATM. VISIT AGAIN")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")

# Start the ATM simulation
atm_simulator()

