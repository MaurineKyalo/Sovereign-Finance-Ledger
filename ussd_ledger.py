# Sovereign Finance Ledger - Day 1 Skeleton

def main_menu():
    print("\n--- Mama Mboga Ledger ---")
    print("1. Record Sale")
    print("2. Record Expense")
    print("3. View Balance")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
    return choice

# Main Program Loop
print("Welcome to the Sovereign Finance Ledger")

while True:
    user_choice = main_menu()
    
    if user_choice == '1':
        print("Sale recording logic will go here.") 
        
    elif user_choice == '2':
        print("Expense recording logic will go here.")
        
    elif user_choice == '3':
        print("Balance calculation will go here.")
        
    elif user_choice == '4':
        print("Exiting system. Goodbye!")
        break
        
    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")