# CodeAlpha_StockTracker

A simple **Stock Portfolio Tracker** built in Python as part of the **CodeAlpha Python Programming Internship**.

## 📌 Task Overview (Task 2)
- **Goal:** Build a simple stock tracker that calculates total investment based on predefined stock prices.
- **Specifications:**
  - Allows users to input stock names (tickers) and quantities.
  - Uses a hardcoded dictionary defining stock prices (e.g., `{"AAPL": 180.00, "TSLA": 250.00, ...}`).
  - Computes subtotal values per holding and displays the overall portfolio investment value.
  - Offers export functionality to save portfolio reports in `.txt` or `.csv` format with timestamps.

## 🛠️ Key Concepts Used
- Python Dictionaries for price lookups
- Console user input/output handling and input validation
- Arithmetic calculations and formatting
- File handling (`.txt` and `.csv` export)

## 🚀 How to Run
1. Make sure Python 3 is installed.
2. Clone the repository:
   ```bash
   git clone https://github.com/abhishek05082007gh-netizen/CodeAlpha_StockTracker.git
   ```
3. Navigate into the directory:
   ```bash
   cd CodeAlpha_StockTracker
   ```
4. Run the script:
   ```bash
   python stock_tracker.py
   ```

## 📊 Sample Output
```text
=======================================================
             PORTFOLIO INVESTMENT SUMMARY             
=======================================================
Stock      Quantity   Price ($)       Subtotal ($)   
-------------------------------------------------------
AAPL       5          $180.00         $900.00        
TSLA       2          $250.00         $500.00        
-------------------------------------------------------
TOTAL INVESTMENT VALUE:               $1400.00       
=======================================================
```
