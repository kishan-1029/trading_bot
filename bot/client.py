from binance.client import Client
import os
from dotenv import load_dotenv

load_dotenv()

def get_client():
    api_key = os.getenv("API_KEY")
    api_secret = os.getenv("API_SECRET")

    # 👇 SPOT testnet disable kar
    client = Client(api_key, api_secret)

    # 👇 FUTURES testnet endpoint set kar (IMPORTANT)
    client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    return client