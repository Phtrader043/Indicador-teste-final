import cohere
from keys import COHERE_API_KEY

co = cohere.Client(COHERE_API_KEY)


def analisar_tendencia(dados, modo):
    prompt = f"""
Você é um analista profissional de mercados financeiros. Analise os seguintes indicadores técnicos para o ativo {dados['ativo']}:
- RSI: {dados['rsi']}
- MACD: {dados['macd']}
- EMA: {dados['ema']}
- ADX: {dados['adx']}
- Bollinger Bands: Superior {dados['bb_upper']}, Inferior {dados['bb_lower']}
- Preço Atual: {dados['price']}

Modo de operação: {modo} (Mais conservador ou agressivo)

Responda apenas no formato JSON:
{{
"Tendencia":"Compra ou Venda ou Neutro",
"Confianca":"(em %)"
}}
"""

    resposta = co.generate(
        model='command',
        prompt=prompt,
        max_tokens=200
    )

    try:
        output = resposta.generations[0].text.strip()
        resultado = eval(output)
        return {
            "tendencia": resultado['Tendencia'],
            "confianca": resultado['Confianca']
        }
    except:
        return {"tendencia": "Neutro", "confianca": "0"}
