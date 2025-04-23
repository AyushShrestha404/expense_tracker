def set_budget():
    while True:
        try:
            amount = float(input("Total Budget: Rs."))
            if amount < 0:
                raise ValueError
            return amount
        except ValueError:
            print("Please enter a valid positive number.\n")

def add_transaction(transactions, categories, budget):
    try:
        amount = float(input("How much did you spend? Rs."))
        if amount <= 0:
            print(" Amount must be positive.\n")
            return
        if amount > get_remaining_budget(transactions, budget):
            print("⚠️ Not enough budget left for this transaction.\n")
            return
    except ValueError:
        print(" Invalid amount.\n")
        return

    category = input("What category was it for?(Fooding, Clothing, Housing, Others) ").strip()
    description = input("Add a short description (optional): ").strip()

    categories.add(category)
    transactions.append({
        "amount": amount,
        "category": category,
        "description": description
    })

    print(f" Recorded Rs.{amount:.2f} for '{category}'\n")

def view_transactions(transactions, budget):
    if not transactions:
        print(" No transactions found.\n")
        return

    print("\n Transaction History:")
    for i, t in enumerate(transactions, 1):
        print(f"{i}. Rs.{t['amount']:.2f} - {t['category']} ({t['description']})")
    print(f"\n Remaining Budget: Rs.{get_remaining_budget(transactions, budget):.2f}\n")

def get_remaining_budget(transactions, budget):
    spent = sum(t["amount"] for t in transactions)
    return budget - spent

def run_tracker():
    print("=== Welcome to the Expense Tracker ===\n")
    budget = set_budget()
    transactions = []
    categories = set()

    while True:
        print("======== MENU ========")
        print("1. Add a transaction")
        print("2. View transactions")
        print("3. View remaining budget")
        print("4. Exit")
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_transaction(transactions, categories, budget)
        elif choice == "2":
            view_transactions(transactions, budget)
        elif choice == "3":
            print(f" Remaining Budget: Rs.{get_remaining_budget(transactions, budget):.2f}\n")
        elif choice == "4":
            print(" Exiting. Stay within budget!")
            break
        else:
            print(" Invalid choice. Try again.\n")

# Run the tracker
run_tracker()
