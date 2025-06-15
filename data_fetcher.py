import requests
from keys import TWELVE_API_KEY
import random


def obter_dados():
    ativo = random.choice(["BTC/USD", "ETH/USD", "EUR/USD", "GBP/USD", "USD/JPY"])

    try:
        price = round(random.uniform(20000, 50000), 2)

        dados = {
            "ativo": ativo,
            "price": price,
            "rsi": random.randint(10, 90),
            "macd": round(random.uniform(-2, 2), 2),
            "ema": round(price * random.uniform(0.95, 1.05), 2),
            "adx": random.randint(10, 50),
            "bb_upper": price + random.uniform(100, 300),
            "bb_lower": price - random.uniform(100, 300)
        }

        return dados
    except:
        return None
