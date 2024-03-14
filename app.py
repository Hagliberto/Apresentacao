import streamlit as st
import pandas as pd
import os
from datetime import datetime
import time
import base64

# Configuração da página Streamlit
st.set_page_config(page_title="Auxílio Educação - NUPNN", page_icon="💧", layout="wide", menu_items={
    "About": "https://ucsb-nupnn.streamlit.app/"})
st.header("🚸`Lançamentos` - Auxílio Educação")

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


def setup_page():
    # Coloque aqui o código para configurar a página do Streamlit
    pass



# Recuperar a senha do segredo
PASSWORD = os.environ.get("PASSWORD")

if PASSWORD is None:
    raise ValueError("A variável de ambiente PASSWORD não está definida.")

# Função para autenticar o usuário
def authenticate():
    st.sidebar.info("`Núcleo de Pessoal Natal Norte`")
    st.sidebar.success("🏫 🚸 Auxílio-Creche | Auxílio-Babá")
    password = st.sidebar.text_input("🔜 `Credencial de Acesso:`", type="password", placeholder='🌐 Digite sua credencial', help=("✅ Podem acessar: Bruna e Hagliberto"))
    if password == PASSWORD:
        st.sidebar.markdown("")  # Ocultar a barra lateral após o login
        st.empty()  # Limpar o campo de senha após o login
        return True
    else:
        st.sidebar.error("❌ Apenas pessoal autorizado!")
        return False



# Autenticar o usuário antes de prosseguir
if authenticate():
    
    # Interface para pesquisa de empregado
    def interface_pesquisa_empregado():
        st.info("🔎 Pesquise o empregado")
        matricula_input = None
        dependente_input = None
        dados_df = pd.DataFrame()  # Definindo um DataFrame vazio inicialmente
        with st.expander("**👷🏻‍♂️ Empregado e 👧🏻👦🏻 Dependente**"):
            col1, col2 = st.columns(2)
            with col1:
                matricula_input = st.number_input("Matrícula: `Digite e pressione enter`", placeholder='🌐 Digite o nome do setor', min_value=0, step=1, help=("⚠️ Alguns empregados possuem mais de um dependente"))
                if matricula_input is None:
                    return None, None
                if not os.path.isfile('dados.xlsx'):
                    st.warning("Por favor, crie a planilha 'dados.xlsx' antes de prosseguir.")
                    return None, None
                dados_df = pd.read_excel('dados.xlsx')
    
                if matricula_input is not None and matricula_input in dados_df['MATRICULA'].values:
                    empregado_nome = dados_df[dados_df['MATRICULA'] == matricula_input]['EMPREGADO'].iloc[0]
                    st.info(f"{empregado_nome}")
                else:
                    warning_message = st.warning("Por favor, digite uma matrícula válida para verificar os dependentes.")
                    time.sleep(5)  # Espera por 5 segundos
                    warning_message.empty()  # Limpa a mensagem de aviso
    
            with col2:
                if matricula_input is not None and matricula_input in dados_df['MATRICULA'].values:
                    dependente_options = dados_df[dados_df['MATRICULA'] == matricula_input]['DEPENDENTE BENEFICIADO'].tolist()
                    if len(dependente_options) > 1:
                        dependente_input = st.selectbox("Dependente:", options=dependente_options)
                        st.error("⚠️ Existem múltiplos dependentes associados a esta matrícula.")
                    elif len(dependente_options) == 1:
                        dependente_input = dependente_options[0]
                        dependente_nome = dados_df[(dados_df['MATRICULA'] == matricula_input) & (dados_df['DEPENDENTE BENEFICIADO'] == dependente_input)]['DEPENDENTE BENEFICIADO'].iloc[0]
                        st.success(f"Dependente associado: {dependente_nome}")
                    else:
                        st.warning("Não foram encontrados dependentes associados a esta matrícula.")
        return matricula_input, dependente_input

    # Função para atualizar os dados do auxílio creche
    def update_auxilio_creche(matricula, valor_apresentado, observacao, tipo_auxilio="Creche", dependente=None, autismo=False, status=None):
        try:
            # Verificar se a matrícula, valor apresentado e observação foram fornecidos
            if matricula is None or valor_apresentado is None or observacao is None:
                st.error("Por favor, preencha todos os campos obrigatórios.")
                return
    
            # Verificar se a planilha dados.xlsx existe
            if not os.path.isfile('dados.xlsx'):
                # Se a planilha não existir, solicitar ao usuário que a crie
                st.warning("A planilha 'dados.xlsx' não foi encontrada no diretório atual.")
                st.warning("Por favor, crie a planilha 'dados.xlsx' antes de prosseguir.")
                return
    
            # Verificar se a planilha Auxilio.xlsx existe
            if not os.path.isfile('Auxilio.xlsx'):
                # Se a planilha não existir, criar uma nova com um DataFrame vazio
                auxilio_creche_df = pd.DataFrame(columns=['MATRICULA', 'EMPREGADO', 'DEPENDENTE BENEFICIADO', 
                                                          'NASCIMENTO', 'IDADE', 'SERIE', 'CNPJ', 'Razão Social', 
                                                          'Valor apresentado', 'À pagar', 'Observação', 'Tipo de Auxílio',
                                                          'Status', 'Data'])
            else:
                # Se a planilha existir, carregar seu conteúdo
                auxilio_creche_df = pd.read_excel('Auxilio.xlsx')
    
            # Carregar dados.xlsx
            dados_df = pd.read_excel('dados.xlsx')
    
            # Verificar se a matrícula existe em dados.xlsx
            if matricula not in dados_df['MATRICULA'].values:
                st.error(f"A matrícula {matricula} não foi encontrada base de empregados.")
                return
    
            # Obter os dados correspondentes à matrícula e dependente
            if dependente is not None:
                dados_matricula = dados_df[(dados_df['MATRICULA'] == matricula) & (dados_df['DEPENDENTE BENEFICIADO'] == dependente)].iloc[0]
            else:
                dados_matricula = dados_df[dados_df['MATRICULA'] == matricula].iloc[0]
    
            # Verificar se o dependente tem menos de 12 anos
            idade_dependente = calcular_idade(dados_matricula['NASCIMENTO'])
            if idade_dependente >= 12:
                st.error(f"O dependente tem atualmente {idade_dependente} anos e não é elegível para receber o auxílio creche.")
                return
    
            # Definir o valor máximo do auxílio de acordo com o tipo de auxílio e a presença de autismo
            if autismo:
                valor_maximo_auxilio = 628.22
            else:
                valor_maximo_auxilio = 314.11
    
            # Calcular o valor a ser pago ou usar o valor fornecido
            if valor_apresentado == "":
                valor_a_pagar = valor_maximo_auxilio  # Ajuste no cálculo
            else:
                # Substituir vírgula por ponto e converter para float
                valor_apresentado = valor_apresentado.replace(',', '.')
                valor_a_pagar = min(float(valor_apresentado), valor_maximo_auxilio)
    
            # Adicionar nova entrada aos dados em Auxilio.xlsx
            nova_entrada = {
                'MATRICULA': f"{matricula:06}",  # Formatando para 6 dígitos sem pontos nem vírgulas
                'EMPREGADO': dados_matricula['EMPREGADO'],
                'DEPENDENTE BENEFICIADO': dados_matricula['DEPENDENTE BENEFICIADO'],
                'NASCIMENTO': formatar_data_nascimento(dados_matricula['NASCIMENTO']),
                'IDADE': calcular_idade(dados_matricula['NASCIMENTO']),
                'SERIE': dados_matricula['SERIE'],
                'CNPJ': dados_matricula['CNPJ'],
                'Razão Social': dados_matricula['Razão Social'],
                'Valor apresentado': formatar_valor(valor_apresentado),  # Corrigindo aqui
                'À pagar': formatar_valor(valor_a_pagar),
                'Observação': observacao,
                'Tipo de Auxílio': tipo_auxilio,
                'Status': status if status else "⚠️ Pendente",  # Definindo o status como pendente por padrão
                'Data': datetime.now().strftime('%d/%m/%Y')  # Adicionando data
            }
            auxilio_creche_df = pd.concat([auxilio_creche_df, pd.DataFrame([nova_entrada])], ignore_index=True)
    
            # Salvar as alterações em Auxilio.xlsx
            auxilio_creche_df.to_excel('Auxilio.xlsx', index=False)
    
            # Mensagem de sucesso ao atualizar os dados
            success_message = st.empty()
            success_message.success("Os dados foram atualizados com sucesso!")
    
            # Aguarda por 2 segundos antes de limpar a mensagem
            time.sleep(2)
    
            # Limpa a mensagem de sucesso após 2 segundos
            success_message.empty()
    
    
        except Exception as e:
            st.error("Por favor, verifique os dados e tente novamente.")
            st.error(str(e))  # Mostra a mensagem de erro específica
    
    # Defina sua função download_auxilio_xlsx() para retornar os dados do arquivo
    def download_auxilio_xlsx():
        if os.path.isfile('Auxilio.xlsx'):
            with open('Auxilio.xlsx', 'rb') as f:
                data = f.read()
            return data
        else:
            st.warning("O arquivo 'Auxilio.xlsx' ainda não foi criado.")

    # Função para baixar a planilha em formato CSV
    def download_auxilio_csv():
        if os.path.isfile('Auxilio.xlsx'):
            auxilio_df = pd.read_excel('Auxilio.xlsx')
            # Criar um DataFrame com as colunas desejadas
            csv_df = pd.DataFrame({
                'Matricula': auxilio_df['MATRICULA'],
                'Verba': [113 if 'creche' in tipo.lower() else (152 if 'babá' in tipo.lower() else None) for tipo in auxilio_df['Tipo de Auxílio']],
                'À pagar': auxilio_df['À pagar']
            })
            # Salvar o DataFrame como CSV
            csv_df.to_csv('Auxilio.csv', index=False)
            # Ler o arquivo CSV e retornar os dados
            with open('Auxilio.csv', 'rb') as f:
                data = f.read()
            return data
        else:
            st.warning("O arquivo 'Auxilio.xlsx' ainda não foi criado.")


    # Função para excluir linha
    def delete_row(index):
        try:
            auxilio_creche_df = pd.read_excel('Auxilio.xlsx')
            auxilio_creche_df.drop(index, inplace=True)
            auxilio_creche_df.to_excel('Auxilio.xlsx', index=False)
            st.success("Linha excluída com sucesso!")
        except Exception as e:
            st.error("Ocorreu um erro ao excluir a linha.")
            st.error(str(e))


    # Função para excluir todas as informações
    def delete_all_data():
        try:
            if os.path.isfile('Auxilio.xlsx'):
                # Remover todas as linhas do arquivo Auxilio.xlsx
                auxilio_creche_df = pd.DataFrame(columns=['MATRICULA', 'EMPREGADO', 'DEPENDENTE BENEFICIADO', 
                                                          'NASCIMENTO', 'IDADE', 'SERIE', 'CNPJ', 'Razão Social', 
                                                          'Valor apresentado', 'À pagar', 'Observação', 'Tipo de Auxílio',
                                                          'Status', 'Data'])
                auxilio_creche_df.to_excel('Auxilio.xlsx', index=False)
                st.success("Todas as informações foram excluídas com sucesso!")
            else:
                st.warning("Nenhum dado foi encontrado para exclusão.")
        except Exception as e:
            st.error("Ocorreu um erro ao excluir todas as informações.")
            st.error(str(e))
    
    
    
    
    # Função para calcular a idade com base na data de nascimento
    def calcular_idade(data_nascimento):
        data_atual = datetime.now()
        data_nascimento = pd.to_datetime(data_nascimento, format='%d/%m/%Y')
        idade = (data_atual - data_nascimento).days // 365
        return idade
    
    # Função para formatar a data de nascimento
    def formatar_data_nascimento(data_nascimento):
        if isinstance(data_nascimento, str):
            data_nascimento = pd.to_datetime(data_nascimento, format='%d/%m/%Y')
        return data_nascimento.strftime('%d/%m/%Y')
    
    # Função para formatar o valor
    def formatar_valor(valor):
        try:
            if isinstance(valor, str):
                # Se for uma matrícula, retorne o valor sem aplicar formatação
                if valor.isdigit():
                    return f'R${float(valor):,.2f}'  # Adiciona o prefixo "R$" e formata o valor
                # Caso contrário, faça a formatação normal
                valor = valor.strip()
                valor = valor.replace(',', '.')
                valor = ''.join(filter(lambda char: char.isdigit() or char == '.', valor))
                valor = float(valor)
        except ValueError:
            st.error("Por favor, insira um valor numérico válido no campo de Valor Apresentado.")
            return None
        return f'R${valor:.2f}'
    
    
    
    # Função para verificar se os campos obrigatórios foram preenchidos
    def campos_obrigatorios_preenchidos(matricula_input, valor_apresentado_input):
        if matricula_input is None or valor_apresentado_input == "":
            st.error("Por favor, informe o valor apresentado no recibo de pagamento escolar.")
            return False
        return True
    
    
    # Interface para valor e observação
    def interface_valor_observacao(matricula_input, dependente_input):
        if matricula_input is None:
            st.error("Por favor, selecione uma matrícula válida.")
            return
    
        st.success("🧮 Informe o valor apresentado uma descrição e a categoria")
        with st.expander("💸**Valor Apresentado e Observação**"):
            col1, col2, col3 = st.columns([2, 4, 2])
            with col1:
                valor_apresentado_input = st.text_input("Valor Apresentado: `Obrigatório`", placeholder='💸 Informe o Valor do Recibo', help=("⚠️ Insira o valor constante no recibo de pagamento!"))
                status_input = st.selectbox("Situação", ["⚠️ Pendente", "🆗 Inserido no TOTVS", "❌ Rejeitado", "✅ Aprovado"], help=("Informe a situação atual"))
            with col2:
                observacao_input = st.text_area("Anotações:", placeholder='📋 Por favor, informe aqui qualquer informação relevante sobre a situação do pagamento do auxílio creche ou babá, meses anteriores, documentos enviados, entre outros detalhes importantes!', help=("⚠️ Adicione informações sobre o comprovante apresentado!"))
            with col3:
                tipo_auxilio_input = st.radio("`Categoria de Auxílio:`", ["Creche", "Babá"], help=("Escolhas as opções disponíveis"))
                autismo_input = st.checkbox("TDAH", help=("Marque se a criança possui TDAH"))
                if st.button("🔜 `Lançar informações`"):
                    if campos_obrigatorios_preenchidos(matricula_input, valor_apresentado_input):
                        tipo_auxilio = tipo_auxilio_input
                        autismo = autismo_input  # Passa o valor do checkbox
                        if autismo_input:
                            tipo_auxilio += " (TDAH)"
                        update_auxilio_creche(matricula_input, valor_apresentado_input, observacao_input, tipo_auxilio, dependente_input, autismo, status_input)
                        # Redefine os campos após a atualização
                        matricula_input = ""  # Limpa o campo de matrícula
                        valor_apresentado_input = ""  # Limpa o campo de valor apresentado
                        observacao_input = ""  # Limpa o campo de observação
                        # Se houver outros campos que precisam ser limpos, faça o mesmo para eles
                
    # Função para baixar a planilha em formato xlsx
    def download_auxilio_xlsx():
        if os.path.isfile('Auxilio.xlsx'):
            # Se o arquivo existir, fazer o download
            with open('Auxilio.xlsx', 'rb') as f:
                data = f.read()
            st.download_button(label="Download Auxilio.xlsx", data=data, file_name='Auxilio.xlsx', mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        else:
            st.warning("O arquivo 'Auxilio.xlsx' ainda não foi criado.")
    
    

    # Função para mostrar os dados já lançados
    def mostrar_dados_lancados():
        try:
            auxilio_creche_df = pd.read_excel('Auxilio.xlsx')
        except FileNotFoundError:
            st.warning("Nenhum dado foi lançado ainda.")
            return

        st.dataframe(auxilio_creche_df)  # Mostra o DataFrame


    def download_button(file_name, data, label):
        b64_data = base64.b64encode(data).decode('utf-8')
        href = f'data:application/octet-stream;base64,{b64_data}'
        st.markdown(f'<a href="{href}" download="{file_name}"><button class="download-button">{label}</button></a>', unsafe_allow_html=True)
    
    


        # Função para atualizar a situação dos dados lançados
    def update_situacao(index, situacao):
        try:
            auxilio_creche_df = pd.read_excel('Auxilio.xlsx')
            auxilio_creche_df.at[index, 'Status'] = situacao
            auxilio_creche_df.to_excel('Auxilio.xlsx', index=False)
            st.success("Situação atualizada com sucesso!")
            # Atualiza a página
            st.experimental_rerun()
        except Exception as e:
            st.error("Ocorreu um erro ao atualizar a situação.")
            st.error(str(e))


    # Função para interface de atualização de situação
    def interface_atualizar_situacao():
        st.info("🛠️ Atualizar Situação")
        index_input = st.number_input("Índice da linha:", min_value=0, step=1)
        situacao_input = st.selectbox("Situação:", ["⚠️ Pendente", "🆗 Inserido no TOTVS", "❌ Rejeitado", "✅ Aprovado"])
        if st.button("Atualizar"):
            update_situacao(index_input, situacao_input)


    # Interface do Streamlit
    # Função principal
    def main():
        setup_page()
    
        expander_col1, expander_col2 = st.columns([2,3])
    
        with expander_col1:
            matricula_input, dependente_input = interface_pesquisa_empregado()
    
        with expander_col2:
            interface_valor_observacao(matricula_input, dependente_input)
            
        with st.expander("**Visualize as informações que já foram lançadas**"):
            mostrar_dados_lancados()
    
        expander_col1, expander_col2, expander_col3, expander_col4, expander_col5 = st.columns(5)
        
        
        with expander_col1:
            # Atualizar situação
            with st.expander("**🛠️ Atualizar Situação**"):
                interface_atualizar_situacao()
         
        with expander_col2:
            with st.expander("💹 **Baixar a Planilha**"):
                st.write("Geralmente, os dados devem ser salvos no último ou primeiro dia do mês.")
                
                # Botão para baixar em formato XLSX
                if st.button("✅ Consolidar dados em XLSX"):
                    st.write("Baixe a planilha em formato XLSX para análise ou referência.")
                    data_xlsx = download_auxilio_xlsx()
                    if data_xlsx is not None:
                        download_button("Auxilio.xlsx", data_xlsx, "Download Auxilio.xlsx")
                
                # Botão para baixar em formato CSV
                if st.button("✅ Consolidar dados em CSV"):
                    st.write("Baixe a planilha em formato CSV para importação no TOTVS.")
                    data_csv = download_auxilio_csv()
                    if data_csv is not None:
                        download_button("Auxilio.csv", data_csv, "Baixar Planilha CSV")
        
        
         
        with expander_col5:
            # Excluir linha
            with st.expander("`♻️ Excluir Linhas`"):
                st.error("🚫 Informe a linha que você deseja excluir!")
                index_to_delete = st.number_input("Índice da Linha para Excluir", min_value=0, step=1)
                if st.button("❌ Excluir", help=("⚠️ Antes de excluir as linhas, faça um beckup dos dados!")):
                    delete_row(index_to_delete)
                    # Atualizar a página
                    st.experimental_rerun()
        
        with expander_col5:
            # Excluir todas as informações
            with st.expander("`♻️ Excluir Todas as Informações`"):
                st.error("🚮 Essa ação irá excluir todos os dados!")
                if st.button("❌ Apagar Tudo", help=("⚠️ Antes de apagar toda a planilha, faça um beckup dos dados!")):
                    delete_all_data()
                    # Atualizar a página
                    st.experimental_rerun() 
    
    # Chamando a função principal
    if __name__ == "__main__":
        setup_page()  # Chama setup_page() aqui para garantir que seja chamado antes de main()
        main()
        
else:
    # Adicionando uma imagem antes do login, apenas se o login não foi bem-sucedido
    st.image("https://maisautomotive.com.br/wp-content/uploads/2022/11/shutterstock_599426126_Easy-Resize.com_.jpg", use_column_width=True)
    st.success("🗝️ `Você precisa de uma credencial válida para acessar o sistema!`")
    
 
