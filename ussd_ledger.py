# Sovereign Finance Ledger - Day 1 Skeleton

def main_menu():
    print("\n--- Mama Mboga Ledger ---")
    print("1. Record Sale")
    print("2. Record Expense")
    print("3. View Balance")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
    return choice

def record_sale():
    while True:
        user_input = input("Enter sale amount (or 0 to go back): KSh ")
        
        # 1. Check for the back button
        if user_input == '0':
            print("Returning to main menu...")
            return 0.0
        
        # 2. Try to convert to float
        try:
            amount = float(user_input)
            
            # 3. Check if they typed a negative number
            if amount <= 0:
                print("Error: Amount must be greater than zero.")
                continue # This jumps back to the top of the loop
            
            # 4. Success!
            print(f"Successfully recorded sale of KSh {amount}")
            return amount
            
        except ValueError:
            print("Error: That's not a number. Try again.")
total_sales = 0.0
print("Welcome to the Sovereign Finance Ledger")

while True:
    user_choice = main_menu()
    
    if user_choice == '1':
        sale_amount = record_sale()
        total_sales += sale_amount

    elif user_choice == '2':
        print("Expense recording logic will go here.")
        
    elif user_choice == '3':
        print(total_sales)
        
    elif user_choice == '4':
        print("Exiting system. Goodbye!")
        break
        
    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")