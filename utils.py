import streamlit as st


def salvar_historico(sinal):
    if 'historico' not in st.session_state:
        st.session_state['historico'] = []

    st.session_state['historico'].append(sinal)


def exibir_historico():
    if 'historico' in st.session_state and st.session_state['historico']:
        for sinal in st.session_state['historico'][-5:][::-1]:
            st.info(f"""### 🔔 Sinal:
- **Ativo:** {sinal['ativo']}
- **Tipo:** {sinal['tipo']}
- **Entrada:** {sinal['entrada']}
- **Saída:** {sinal['saida']}
- **Tendência:** {sinal['tendencia']}
""")
    else:
        st.info("Nenhum sinal gerado ainda.")
