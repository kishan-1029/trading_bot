# 🚀 Trading Bot (Binance Futures Testnet)

A Python-based CLI trading bot that places MARKET and LIMIT orders on Binance Futures Testnet (USDT-M).
This project demonstrates clean architecture, proper validation, logging, and real API integration.

---

## 📌 Features

* Place MARKET and LIMIT orders
* Supports both BUY and SELL
* Uses Binance Futures Testnet API
* CLI-based input using argparse
* Input validation (symbol, side, type, quantity, price)
* Structured code (client, orders, validators, CLI)
* Logging of API requests, responses, and errors
* Exception handling (invalid input, API errors, network issues)

---

## 🏗️ Project Structure

trading_bot/

├── bot/
│   ├── **init**.py
│   ├── client.py          # Binance API client
│   ├── orders.py          # Order placement logic
│   ├── validators.py      # Input validation
│   ├── logging_config.py  # Logging setup

├── logs/
│   └── app.log

├── cli.py
├── requirements.txt
└── README.md

---

## ⚙️ Setup Instructions

### 1. Clone the repository

git clone <your-repo-link>
cd trading_bot

---

### 2. Install dependencies

pip install -r requirements.txt

---

### 3. Setup environment variables

Create a `.env` file in root directory:

API_KEY=your_api_key
API_SECRET=your_api_secret

---

### 4. Binance Testnet Setup

* Open Binance Futures Testnet
* Login and create API keys
* Ensure testnet balance is available

---

## ▶️ How to Run

### MARKET Order

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01

---

### LIMIT Order

python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 80000

---

## 📊 Sample Output

📊 Order Summary
{'symbol': 'BTCUSDT', 'side': 'BUY', 'type': 'MARKET', 'quantity': 0.01}

🔍 Full API Response:
{...}

✅ Order Executed Successfully
Order ID: 123456
Status: NEW
Executed Qty: 0.0000
Avg Price: 0.00

---

## 📝 Logs

Logs are stored in:

logs/app.log

Includes:

* API requests
* API responses
* Errors

---

## ⚠️ Notes

* LIMIT orders may remain in "NEW" status until market price matches
* MARKET orders execute immediately based on liquidity
* Price rules:

  * BUY LIMIT → price below market
  * SELL LIMIT → price above market

---

## 🧠 Assumptions

* User has valid Binance Testnet API credentials
* User has testnet balance
* VPN may be required depending on region

---

## 🚀 Future Improvements

* Stop-Limit / OCO orders
* Interactive CLI
* UI dashboard
* Order tracking

---

## 👨‍💻 Author

Kishan Vasita

---

## ✅ Conclusion

This project demonstrates real-world API integration, CLI design, and clean code practices required for a trading bot system.
