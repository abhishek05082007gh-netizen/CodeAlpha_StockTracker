"""
CodeAlpha Internship - Task 2: Stock Portfolio Tracker
Author: Abhishek Singh
Description: A simple stock portfolio tracker that calculates total investment value
             based on a hardcoded stock price dictionary and supports saving reports to file (.txt or .csv).
"""

import csv
from datetime import datetime

# Hardcoded stock price dictionary ($ USD per share)
STOCK_PRICES = {
    "AAPL": 180.00,
    "TSLA": 250.00,
    "MSFT": 420.00,
    "GOOGL": 175.00,
    "AMZN": 185.00,
    "NVDA": 120.00,
    "META": 500.00,
    "NFLX": 620.00
}

def display_available_stocks():
    print("\n--- Available Stocks & Prices ---")
    print(f"{'Ticker':<10} {'Price ($)':<10}")
    print("-" * 25)
    for ticker, price in STOCK_PRICES.items():
        print(f"{ticker:<10} ${price:<10.2f}")
    print("-" * 25)

def get_portfolio_data():
    portfolio = {}
    display_available_stocks()
    print("\nAdd stocks to your portfolio. Type 'DONE' when finished.")

    while True:
        ticker = input("\nEnter Stock Ticker (or 'DONE'): ").strip().upper()

        if ticker == "DONE":
            if not portfolio:
                print("Your portfolio is currently empty.")
                choice = input("Are you sure you want to finish? (y/n): ").strip().lower()
                if choice == "y":
                    break
                else:
                    continue
            break

        if ticker not in STOCK_PRICES:
            print(f"❌ Error: '{ticker}' is not in the price list. Available tickers: {', '.join(STOCK_PRICES.keys())}")
            continue

        try:
            quantity_input = input(f"Enter quantity of shares for {ticker}: ").strip()
            quantity = int(quantity_input)
            if quantity <= 0:
                print("⚠️ Quantity must be a positive integer.")
                continue
        except ValueError:
            print("⚠️ Invalid quantity! Please enter an integer.")
            continue

        # Add or update portfolio
        portfolio[ticker] = portfolio.get(ticker, 0) + quantity
        print(f"✅ Added {quantity} share(s) of {ticker}. Total: {portfolio[ticker]}")

    return portfolio

def calculate_portfolio_summary(portfolio):
    summary = []
    total_value = 0.0

    for ticker, qty in portfolio.items():
        price = STOCK_PRICES[ticker]
        subtotal = price * qty
        total_value += subtotal
        summary.append({
            "ticker": ticker,
            "quantity": qty,
            "price": price,
            "subtotal": subtotal
        })

    return summary, total_value

def display_summary(summary, total_value):
    print("\n" + "=" * 55)
    print("             PORTFOLIO INVESTMENT SUMMARY             ")
    print("=" * 55)
    print(f"{'Stock':<10} {'Quantity':<10} {'Price ($)':<15} {'Subtotal ($)':<15}")
    print("-" * 55)
    for item in summary:
        print(f"{item['ticker']:<10} {item['quantity']:<10} ${item['price']:<14.2f} ${item['subtotal']:<14.2f}")
    print("-" * 55)
    print(f"{'TOTAL INVESTMENT VALUE:':<37} ${total_value:<15.2f}")
    print("=" * 55)

def save_to_file(summary, total_value):
    if not summary:
        return

    print("\n--- Export Portfolio ---")
    print("1. Save as Text File (.txt)")
    print("2. Save as CSV File (.csv)")
    print("3. Skip Saving")

    choice = input("Choose an option (1-3): ").strip()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if choice == "1":
        filename = "portfolio_summary.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write("=" * 55 + "\n")
            f.write("             PORTFOLIO INVESTMENT SUMMARY             \n")
            f.write(f"Generated on: {timestamp}\n")
            f.write("=" * 55 + "\n")
            f.write(f"{'Stock':<10} {'Quantity':<10} {'Price ($)':<15} {'Subtotal ($)':<15}\n")
            f.write("-" * 55 + "\n")
            for item in summary:
                f.write(f"{item['ticker']:<10} {item['quantity']:<10} ${item['price']:<14.2f} ${item['subtotal']:<14.2f}\n")
            f.write("-" * 55 + "\n")
            f.write(f"{'TOTAL INVESTMENT VALUE:':<37} ${total_value:<15.2f}\n")
            f.write("=" * 55 + "\n")
        print(f"✅ Successfully saved portfolio summary to '{filename}'!")

    elif choice == "2":
        filename = "portfolio_summary.csv"
        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Stock Ticker", "Quantity", "Price ($)", "Subtotal ($)"])
            for item in summary:
                writer.writerow([item["ticker"], item["quantity"], f"{item['price']:.2f}", f"{item['subtotal']:.2f}"])
            writer.writerow([])
            writer.writerow(["TOTAL INVESTMENT VALUE", "", "", f"{total_value:.2f}"])
            writer.writerow(["Generated On", timestamp, "", ""])
        print(f"✅ Successfully saved portfolio summary to '{filename}'!")
    else:
        print("Saving skipped.")

def main():
    print("\n" + "=" * 55)
    print("     CODEALPHA - STOCK PORTFOLIO TRACKER     ")
    print("=" * 55)

    portfolio = get_portfolio_data()
    if not portfolio:
        print("\nNo stocks were tracked. Exiting.")
        return

    summary, total_value = calculate_portfolio_summary(portfolio)
    display_summary(summary, total_value)
    save_to_file(summary, total_value)

    print("\nThank you for using CodeAlpha Stock Portfolio Tracker!\n")

if __name__ == "__main__":
    main()
