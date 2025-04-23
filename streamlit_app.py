import streamlit as st

st.title('🎈 Projeto para a disciplina de Inteligência Artificial')

st.write('Este projeto tem como intuito fazer a análise preditiva\n'
         'da aprovação de empréstimos.')

# Inputs do usuário com novas variáveis

no_of_dependents = st.selectbox('Número de Dependentes', [0, 1, 2, 3])
education = st.selectbox('Graduado?', [0, 1])  # 0 = Graduate, 1 = Not Graduate
self_employed = st.selectbox('Autônomo?', [0, 1])
income_annum = st.number_input('Renda Anual do Solicitante', min_value=0)
loan_amount = st.number_input('Valor do Empréstimo', min_value=0)
loan_term = st.number_input('Prazo do Empréstimo (em meses)', min_value=0)
cibil_score = st.selectbox('Histórico de Crédito (CIBIL Score)', [0, 1])
residential_assets_value = st.number_input('Valor dos Bens Residenciais', min_value=0)
commercial_assets_value = st.number_input('Valor dos Bens Comerciais', min_value=0)
luxury_assets_value = st.number_input('Valor dos Bens de Luxo', min_value=0)
bank_asset_value = st.number_input('Valor dos Bens Bancários', min_value=0)


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