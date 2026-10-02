# CodeAlpha Stock Portfolio Tracker

# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 420,
    "AMZN": 180
}

portfolio = {}
total_investment = 0

print("======================================")
print("      STOCK PORTFOLIO TRACKER")
print("======================================")

print("\nAvailable stocks:")
for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")

while True:
    stock_name = input("\nEnter stock name (or 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("Stock not available. Please choose from the listed stocks.")
        continue

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            continue

        portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity

    except ValueError:
        print("Please enter a valid number for quantity.")

print("\n======================================")
print("          PORTFOLIO SUMMARY")
print("======================================")

for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    value = price * quantity
    total_investment += value

    print(f"{stock}: {quantity} shares × ${price} = ${value}")

print("--------------------------------------")
print(f"Total Investment Value: ${total_investment}")
print("======================================")
print("Thank you for using the Stock Portfolio Tracker!")