import streamlit as st

def main():
    st.title('Portfólio de Projetos')

    st.success("""
    𝐍𝐞𝐬𝐭𝐚 𝐩𝐚́𝐠𝐢𝐧𝐚, 𝐯𝐨𝐜𝐞̂ 𝐞𝐧𝐜𝐨𝐧𝐭𝐫𝐚𝐫𝐚́ 𝐮𝐦𝐚 𝐥𝐢𝐬𝐭𝐚 𝐝𝐨𝐬 𝐦𝐞𝐮𝐬 𝐩𝐫𝐨𝐣𝐞𝐭𝐨𝐬, 𝐣𝐮𝐧𝐭𝐚𝐦𝐞𝐧𝐭𝐞 𝐜𝐨𝐦 𝐨𝐬 𝐥𝐢𝐧𝐤𝐬 𝐩𝐚𝐫𝐚 𝐚𝐜𝐞𝐬𝐬𝐚́-𝐥𝐨𝐬.
    """)

    # Dividindo a tela em duas colunas
    col1, col2 = st.columns(2)

    # Coluna 1
    with col1:
        st.subheader('`Projetos:` Recursos Humanos')

        st.markdown('- 🗓️[Calendário de Escalas](https://hagliberto-calendario-de-escalas.streamlit.app/)')
        st.markdown('- 📝[Lançamentos do Setor](https://teste-lancamentos-do-setor.streamlit.app/)')
        st.markdown('- 🚸[Auxílio Educação](https://hagliberto-creche-testes.streamlit.app/)')
        st.markdown('- #####  ☎️ [`Lista Telefônica da CAERN`](https://lista-telefonica-caern.streamlit.app/)')
        st.markdown('- #####  🚗 🚒 🚜[𝕍𝕖𝕣𝕓𝕒 1️⃣5️⃣4️⃣ - `Adicional Temporário de Condução de Veículos`](https://hagliberto-atcv.streamlit.app/)')
        st.markdown('- #####  [𝕍𝕖𝕣𝕓𝕒 4️⃣1️⃣6️⃣ `Faltas` | 𝕍𝕖𝕣𝕓𝕒 4️⃣9️⃣3️⃣ `DSR sobre Faltas`](https://hagliberto-dsr.streamlit.app/)')
        
    # Coluna 2
    with col2:
        st.subheader('`Projetos:` OiTchau')
        
        st.markdown('- ##### 🔁[𝑱𝒖𝒏𝒕𝒂𝒓 𝑷𝒍𝒂𝒏𝒊𝒍𝒉𝒂𝒔`⏰Horas e 📊Sumário`](https://hagliberto-unir-planilhas.streamlit.app/)')     
        st.markdown('#####  [𝕍𝕖𝕣𝕓𝕒 1️⃣3️⃣5️⃣ - `Adicional Noturno`](https://hagliberto-verba135.streamlit.app/)')
        st.markdown('#####  [𝕍𝕖𝕣𝕓𝕒 1️⃣3️⃣6️⃣ - `Horas 50%`](https://hagliberto-verba136.streamlit.app/)')
        st.markdown('#####  [𝕍𝕖𝕣𝕓𝕒 1️⃣3️⃣7️⃣ - `Horas 100%`](https://hagliberto-verba137.streamlit.app/)')
        st.markdown('#####  [𝕍𝕖𝕣𝕓𝕒 1️⃣4️⃣5️⃣ - `Ajuda de Custo`](https://hagliberto-verba145.streamlit.app/)')
        st.markdown('#####  [𝕍𝕖𝕣𝕓𝕒 1️⃣4️⃣7️⃣ - `Intrajornada`](https://hagliberto-verba147.streamlit.app/)')
        st.markdown('- #####  🔃 [𝑱𝒖𝒏𝒕𝒂𝒓 𝒂𝒔 𝑽𝒆𝒓𝒃𝒂𝒔 `135` `136` `137` `145` `147`](https://hagliberto-unir-verbas.streamlit.app/)')
        st.markdown('- #####  ⬅️🚹➡️[𝐒𝐞𝐩𝐚𝐫𝐚𝐫 𝐄𝐦𝐩𝐫𝐞𝐠𝐚𝐝𝐨𝐬 𝐝𝐞 𝐄𝐬𝐜𝐚𝐥𝐚𝐬 - 1️⃣2️⃣❎3️⃣6️⃣ e 2️⃣4️⃣❎7️⃣2️⃣](https://hagliberto-calcular-8e16.streamlit.app/)')
        st.markdown('- #####  📈 [𝑭𝒐𝒍𝒉𝒂 𝒅𝒆 𝑭𝒓𝒆𝒒𝒖𝒆𝒏𝒄𝒊𝒂 - `Análise detalhada`](https://hagliberto-frequencia.streamlit.app/)')
        
if __name__ == '__main__':
    main()
