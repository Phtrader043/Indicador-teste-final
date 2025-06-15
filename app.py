import streamlit as st
from signal_engine import gerar_sinal
from utils import exibir_historico, tocar_alerta
import time
import pytz
from datetime import datetime


# =========================
# 🎨 Configuração da Página
# =========================
st.set_page_config(
    page_title="Indicador GPT 1.0 - Equipe PHTrader",
    layout="wide",
    page_icon="📊"
)


# =========================
# 🌎 Horário de Brasília
# =========================
fuso_brasilia = pytz.timezone('America/Sao_Paulo')
agora = datetime.now(fuso_brasilia).strftime("%d/%m/%Y %H:%M:%S")


# =========================
# 🎯 Sidebar de Configuração
# =========================
st.sidebar.title("⚙️ Configurações")

modo = st.sidebar.selectbox(
    "🎯 Escolha o Modo:",
    ["Conservador", "Agressivo"],
    key="select_modo"
)

ativar_ia = st.sidebar.toggle(
    "🚀 Ativar IA",
    value=False,
    key="toggle_ativar_ia"
)

st.sidebar.markdown("---")
st.sidebar.caption(f"🕒 Horário de Brasília: {agora}")


# =========================
# 🏠 Título Principal
# =========================
st.title("📈 Indicador GPT 1.0 - Equipe PHTrader")
st.subheader("🔍 Monitoramento de Cripto & Forex com IA e Análise Técnica")
st.markdown("---")


# =========================
# 🖥️ Área Principal
# =========================
col1, col2 = st.columns(2)

with col1:
    st.subheader("📢 Últimos Sinais")
    exibir_historico()

with col2:
    st.subheader("🚦 Status do Robô")
    if ativar_ia:
        st.success("🟢 IA ATIVADA - Gerando sinais automaticamente")
    else:
        st.warning("🛑 IA DESATIVADA")


# =========================
# 🔄 Loop de geração de sinais
# =========================
if ativar_ia:
    placeholder = st.empty()

    while True:
        with placeholder.container():
            sinal = gerar_sinal(modo)

            if sinal:
                st.success(
                    f"✅ Novo sinal detectado: {sinal['Ativo']} | "
                    f"{sinal['Tipo']} | "
                    f"Entrada: {sinal['Entrada']} | "
                    f"Saída: {sinal['Saída']} | "
                    f"Tendência: {sinal['Tendência']}"
                )

                # 🔊 Emitir alerta sonoro
                tocar_alerta(sinal['Ativo'])

                st.balloons()

            else:
                st.info("🔍 Nenhum sinal identificado no momento.")

            time.sleep(120)  # Espera 2 minutos antes de gerar o próximo sinal

            # Verificar se o usuário desligou a IA
            ativar_ia = st.session_state.get("toggle_ativar_ia", False)
            if not ativar_ia:
                st.warning("🛑 IA DESATIVADA")
                break
else:
    st.info("🔽 Ative a IA no menu lateral para iniciar a geração de sinais.")
