from indicators import analisar_indicadores
from cohere_analysis import analisar_tendencia
from data_fetcher import obter_dados
from datetime import datetime


def gerar_sinal(modo):
    dados = obter_dados()

    if not dados:
        return None

    resultado_indicadores = analisar_indicadores(dados)

    if resultado_indicadores['tendencia'] == 'Neutro':
        return None

    analise_ia = analisar_tendencia(dados, modo)

    if analise_ia['tendencia'] == resultado_indicadores['tendencia']:
        now = datetime.now().strftime('%H:%M')
        saida = (datetime.now().replace(minute=datetime.now().minute + 5)).strftime('%H:%M')
        return {
            "ativo": dados['ativo'],
            "tipo": resultado_indicadores['tendencia'],
            "entrada": now,
            "saida": saida,
            "tendencia": f"{analise_ia['confianca']}%"
        }
    else:
        return None
