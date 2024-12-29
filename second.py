#stock portfolio tracker
def stock_portfolio_tracker():
    portfolio = {}

    while True:
        print("\n1. Add stock")
        print("2. Remove stock")
        print("3. View portfolio")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            stock_symbol = input("Enter stock symbol: ")
            shares = int(input("Enter number of shares: "))
            portfolio[stock_symbol] = shares
        elif choice == "2":
            stock_symbol = input("Enter stock symbol to remove: ")
            if stock_symbol in portfolio:
                del portfolio[stock_symbol]
            else:
                print("Stock not found in portfolio.")
        elif choice == "3":
            for symbol, shares in portfolio.items():
                print(f"{symbol}: {shares} shares")
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

stock_portfolio_tracker() 
