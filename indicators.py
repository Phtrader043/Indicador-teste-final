def analisar_indicadores(dados):
    rsi = dados['rsi']
    macd = dados['macd']
    ema = dados['ema']
    adx = dados['adx']
    bb_upper = dados['bb_upper']
    bb_lower = dados['bb_lower']
    price = dados['price']

    sinais = []

    if rsi < 30:
        sinais.append('Compra')
    elif rsi > 70:
        sinais.append('Venda')

    if macd > 0:
        sinais.append('Compra')
    elif macd < 0:
        sinais.append('Venda')

    if price > ema:
        sinais.append('Compra')
    else:
        sinais.append('Venda')

    if adx > 25:
        tendencia = max(set(sinais), key=sinais.count)
    else:
        tendencia = 'Neutro'

    return {
        "tendencia": tendencia
    }
