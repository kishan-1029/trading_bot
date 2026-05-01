# Trading Bot (Binance Futures Testnet)

## Setup
pip install -r requirements.txt

## Run

### MARKET order
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01

### LIMIT order
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 60000