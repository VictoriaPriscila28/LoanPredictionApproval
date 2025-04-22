import streamlit as st

st.title('🎈 Projeto para a disciplina de Inteligência Artificial')

st.write('Este projeto tem como intuito fazer a análise preditiva\n'
         'da aprovação de empréstimos.')

# Inputs do usuário
renda = st.number_input('Renda do Solicitante', min_value=0)
co_renda = st.number_input('Renda do Co-Solicitante', min_value=0)
loan_amount = st.number_input('Valor do Empréstimo', min_value=0)
loan_term = st.number_input('Prazo do Empréstimo', min_value=0)
credit_history = st.selectbox('Histórico de Crédito', [0, 1])
gender = st.selectbox('Gênero', [0, 1])  # 0 = Female, 1 = Male
married = st.selectbox('Casado?', [0, 1])
education = st.selectbox('Graduado?', [0, 1])  # 0 = Graduate, 1 = Not Graduate
self_employed = st.selectbox('Autônomo?', [0, 1])
dependents = st.selectbox('Dependentes', [0, 1, 2, 3])
property_area = st.selectbox('Área da Propriedade', [0, 1, 2])  # 0=Rural, 1=Semiurban, 2=Urban

# Quando o botão for clicado
if st.button('Verificar Aprovação'):
    input_usuario = np.array([[gender, married, dependents, education, self_employed,
                               renda, co_renda, loan_amount, loan_term,
                               credit_history, property_area]])

    resultado = modelo.predict(input_usuario)

    if resultado[0] == 1:
        st.success('✅ Empréstimo Aprovado!')
    else:
        st.error('❌ Empréstimo Negado.')