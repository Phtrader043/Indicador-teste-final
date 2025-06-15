import requests
import pandas as pd
from datetime import datetime, timedelta
from config import TWELVEDATA_API_KEY

# 🔧 Função para listar todos os pares Forex disponíveis na TwelveData
def listar_pares_forex():
    url = "https://api.twelvedata.com/forex_pairs"
    params = {'apikey': TWELVEDATA_API_KEY}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        return [item['symbol'] for item in data]
    else:
        print(f"Erro ao buscar pares Forex: {response.status_code}")
        return []

# 🔍 Função para coletar candles do ativo
def obter_candles(ativo, intervalo='5min', quantidade=100):
    url = "https://api.twelvedata.com/time_series"
    params = {
        'symbol': ativo,
        'interval': intervalo,
        'outputsize': quantidade,
        'apikey': TWELVEDATA_API_KEY,
        'format': 'JSON'
    }
    response = requests.get(url, params=params)
    dados = response.json()

    if 'values' not in dados:
        print(f"Erro ao obter dados do ativo {ativo}: {dados}")
        return None

    df = pd.DataFrame(dados['values'])
    df = df.astype({
        'open': float,
        'high': float,
        'low': float,
        'close': float,
        'volume': float
    })
    df['datetime'] = pd.to_datetime(df['datetime'])
    df = df.sort_values('datetime')
    return df

# 📊 Função para consultar indicadores técnicos
def obter_indicador(ativo, indicador, params_extra=None):
    url = f"https://api.twelvedata.com/{indicador}"
    params = {
        'symbol': ativo,
        'interval': '5min',
        'apikey': TWELVEDATA_API_KEY,
        'format': 'JSON'
    }
    if params_extra:
        params.update(params_extra)

    response = requests.get(url, params=params)
    data = response.json()

    if 'values' in data:
        df = pd.DataFrame(data['values'])
        df['datetime'] = pd.to_datetime(df['datetime'])
        return df.sort_values('datetime')
    else:
        print(f"Erro no indicador {indicador} para {ativo}: {data}")
        return None

# 🔥 Função principal que reúne dados e indicadores
def obter_dados(ativo):
    candles = obter_candles(ativo)

    if candles is None:
        return None

    indicadores = {
        'EMA': obter_indicador(ativo, 'ema', {'time_period': 10}),
        'RSI': obter_indicador(ativo, 'rsi', {'time_period': 14}),
        'MACD': obter_indicador(ativo, 'macd'),
        'ADX': obter_indicador(ativo, 'adx', {'time_period': 14}),
        'BBANDS': obter_indicador(ativo, 'bbands'),
        'STOCH': obter_indicador(ativo, 'stoch')
    }

    return {
        'candles': candles,
        'indicadores': indicadores
    }

# ✅ Teste rápido
if __name__ == "__main__":
    pares = listar_pares_forex()
    print("Total de pares encontrados:", len(pares))
    print(pares[:10])  # Mostra os 10 primeiros pares encontrados

    ativo_teste = 'EUR/USD'
    dados = obter_dados(ativo_teste)

    if dados:
        print(f"Candles de {ativo_teste}:")
        print(dados['candles'].tail())

        print(f"Indicadores de {ativo_teste}:")
        for nome, df in dados['indicadores'].items():
            if df is not None:
                print(f"{nome}:")
                print(df.tail())
    
