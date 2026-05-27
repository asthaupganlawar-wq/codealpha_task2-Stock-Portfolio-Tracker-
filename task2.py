# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320,
    "AMZN": 150
}

total_investment = 0

print("===================================")
print("      STOCK PORTFOLIO TRACKER")
print("===================================")

# Number of stocks user wants to enter
n = int(input("How many stocks do you want to add? "))

# Open file to save results
file = open("portfolio.txt", "w")

file.write("Stock Portfolio Details\n")
file.write("========================\n")

for i in range(n):

    stock_name = input("\nEnter stock name: ").upper()

    if stock_name in stock_prices:

        quantity = int(input("Enter quantity: "))

        price = stock_prices[stock_name]
        investment = price * quantity

        total_investment += investment

        print("Investment for", stock_name, "=", investment)

        # Save to file
        file.write(f"{stock_name} - Quantity: {quantity}, Investment: {investment}\n")

    else:
        print("Stock not available.")

print("\nTotal Investment Value =", total_investment)

file.write("\nTotal Investment Value = " + str(total_investment))

file.close()

print("\nPortfolio details saved in portfolio.txt")