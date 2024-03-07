import streamlit as st
import pandas as pd
import os


# Recuperar as senhas dos usuários Bruna, Hagliberto e caern das variáveis de ambiente
bruna_password = os.environ.get("BRUNA_PASSWORD")
hagliberto_password = os.environ.get("HAGLIBERTO_PASSWORD")
caern_password = os.environ.get("CAERN_PASSWORD")

# Verificar se as senhas estão definidas
if bruna_password is None or hagliberto_password is None or caern_password is None:
    raise ValueError("As senhas de Bruna, Hagliberto ou CAERN não estão definidas nas variáveis de ambiente.")

# Função para autenticar o usuário
def authenticate():
    st.sidebar.info("Núcleo de Pessoal Natal Norte")
    st.sidebar.success("📞 `Lista Telefônica da CAERN` ☎️")
    password = st.sidebar.text_input("🔜 `Credencial de Acesso:`", type="password", placeholder='🌐 Digite sua credencial', help=("✅ Podem acessar: Bruna, Hagliberto ou caern"))
    if password == bruna_password or password == hagliberto_password or password == caern_password:
        st.sidebar.empty()  # Limpar a barra lateral após o login
        st.empty()  # Limpar o campo de senha após o login
        return True, "Bruna" if password == bruna_password else "Hagliberto" if password == hagliberto_password else "caern"
    elif password != '' and password != bruna_password and password != hagliberto_password and password != caern_password:
        st.sidebar.error("❌ Senha incorreta! `Tente novamente.`")
    return False, ""

# Autenticar o usuário antes de prosseguir
authenticated, logged_in_user = authenticate()
if authenticated:
   
    def welcome_page():
        st.markdown('### 👋🏻👨🏻‍💻 Bem-vindo(a) às Ferramentas de Formatação de Horas: OiTchau para o TOTVS')
        st.write("Esta é uma aplicação multifuncional que oferece diversas funcionalidades úteis.")
        
        
        # Seção sobre a aplicação
        with st.expander('1️⃣ Sobre a Aplicação'):
            st.subheader('Esta aplicação é eficiente na visualização, manipulação e formatação de dados relacionados a horas trabalhadas.')
            st.text('Projetada para simplificar a otimização de tarefas específicas, economizando tempo e melhorando a produtividade.')
            st.markdown('***')
    
        # Programa 1: Merge de Arquivos
        with st.expander('2️⃣ **Junte os arquivos:** CAERN-Extra Hours All e CAERN-Summary All'):
            st.text('Esta aplicação permite facilmente mesclar dois arquivos de forma intuitiva.')
            st.text('👀 Visualize, selecione e faça o download de colunas específicas, tenha o controle total sobre os dados necessários.')
    
        # Programa 2: Formatação de Colunas
        with st.expander('3️⃣ Formatação de Colunas'):
            st.text('⬅️ Simplifiquei a formatação de diversas verbas. Escolha entre as opções abaixo⬇️:')
            st.markdown('* * **Verba 135:A Adicional Noturno 20%**, esta verba possui um acréscimo de 0,142857 nas horas.*')
            st.markdown('* * **Verba 136:A Horas de 50%**, nela temos as horas extras realizadas de segunda a sábado, das 5h às 22h.*')
            st.markdown('* * **Verba 137:A Horas de 100%**: nela temos as horas extras realizadas em domingos, feriados e pontos facultativos.')
            st.subheader('⚠️Antes de prosseguir, atualize a coluna **Trabalhados⚠️**')
            st.markdown('* * **Ajuda de Custo - Verba 145**:A Nela temos os dias de trabalhos no mês, esta verba possui um acrescimo de ajuda de custo.')
            st.text('Empregados da escala de revezamento recebem Ajuda de Custo por dia trabalhado, quanto à escala:')
            st.markdown('R$12,56 para empregados da jornada (12x36)')
            st.markdown('R$25,13 para empregados da jornada (24x72).')
            st.markdown('* * **Intrajornada - Verba 147**:A Esta verba corresponde aos dias trabalhados*.')
    
        st.markdown('***')
        with st.expander('⚠️ IMPORTANTE'):
            st.markdown('✅ Os empregados (que não trabalham em escala de revezamento), o valor da Ajuda de Custo será de R$31,15 nas situações:')
            st.text('1️⃣ Os trabalhadores, pela necessidade e improrrogabilidade da execução dos serviços,')
            st.text('executarem jornada extraordinária igual ou superior a duas (2) horas da jornada respectiva;')
            st.text('2️⃣ Ou tiverem seu intervalo intrajornada regular suprimido;')
            st.text('3️⃣ Ou prestarem serviços fora do seu domicílio funcional regular,')
            st.text('em situações que não ensejem o pagamento de diárias de serviço, com deslocamento superior a quatro (4) horas.')
    
        # Adicione um link para o Canva
        canva_link = "https://www.canva.com/design/DAFerOSq0MI/shHMVbgUrW-R6qbKOcPUuA/edit?utm_content=DAFerOSq0MI&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton"
        oitchau_link = "https://admin.oitchau.com.br/login"
        Central_de_Ajuda_Oitchau = "https://support.day.io/hc/pt-br"
        Adicional_noturno = "https://www.oitchau.com.br/blog/calcular-adicional-noturno/"
        Horas_extras = "https://www.oitchau.com.br/blog/horas-extras/"
        Jornada_Noturna = "https://tangerino.com.br/blog/jornada-de-trabalho-noturno/"
    
        # Coloque o texto e o link na mesma linha
        with st.expander('🔗Links recomendados ✅'):
            st.write(f' Faça seu login! <a href="{oitchau_link}" target="_blank">Pagina incial do OiTchau</a>', unsafe_allow_html=True)
            st.write(f'<a href="{Central_de_Ajuda_Oitchau}" target="_blank">Central de Ajuda Oitchau:</a> Informações e tutoriais completos', unsafe_allow_html=True)
            st.write(f'<a href="{Adicional_noturno}" target="_blank">Calcular adicional noturno:</a> Veja como fazer! - Julia Neves, 28/07/2023', unsafe_allow_html=True)
            st.write(f'<a href="{Jornada_Noturna}" target="_blank">Jornada de Trabalho Noturno:</a>  Que Você Precisa Saber? - Leonardo Barros, 05/04/2023', unsafe_allow_html=True)
            st.write(f'<a href="{Horas_extras}" target="_blank">Horas Extras:</a> Guia de como fazer uma gestão completa! - Aline Mesquita, 1/07/2023', unsafe_allow_html=True)
            st.write(f'<a href="{canva_link}" target="_blank">Manual - Horas Extras (Oitchau) - Gestores</a> 08/08/2023 - V1.0 - Bruna Silva, 08/08/2023', unsafe_allow_html=True)
    
    
    
    
    
def main():
    st.set_page_config(
        page_title="Hagliberto Alves de Oliveira",
        page_icon="👨🏻‍💻",
        layout="wide",
        initial_sidebar_state="collapsed",  # Expandir a barra lateral por padrão
    )
            
    # Definindo o estilo CSS para o rodapé
    footer_style = """
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: #f0f0f0;
    color: #333;
    text-align: center;
    padding: 10px 0;
    """
    
    # Adicionando o rodapé com o texto "Hagliberto Alves de Oliveira"
    st.markdown(
        """
        <div style='"""+ footer_style +"""'>
            👨🏻‍💻 Hagliberto Alves de Oliveira ®️
        </div>
        """,
        unsafe_allow_html=True
    )

    welcome_page()
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
