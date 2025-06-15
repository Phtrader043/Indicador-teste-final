import streamlit as st


def alerta_sonoro(ativo):
    js_code = f"""
    var msg = new SpeechSynthesisUtterance("ATENÇÃO SENHOR PEDRO, UM NOVO SINAL FOI IDENTIFICADO PARA {ativo}");
    window.speechSynthesis.speak(msg);
    """
    st.components.v1.html(f"<script>{js_code}</script>")
