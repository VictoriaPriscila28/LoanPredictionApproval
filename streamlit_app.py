import streamlit as st
import pickle
import numpy as np

st.title('🎈 Projeto para a disciplina de Inteligência Artificial')

st.write('Este projeto tem como intuito fazer a análise preditiva\n'
         'da aprovação de empréstimos.')

# Carrega o modelo e o scaler
model = pickle.load(open("best_loan_model2.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

st.title("Simulador de Aprovação de Empréstimo")

# Inputs do usuário
no_of_dependents = st.number_input("Número de dependentes", min_value=0)
education = st.selectbox("Educação", ["Graduado", "Não graduado"])
self_employed = st.selectbox("Autônomo", ["Sim", "Não"])
income_annum = st.number_input("Renda anual")
loan_amount = st.number_input("Valor do empréstimo")
loan_term = st.number_input("Prazo do empréstimo (meses)")
cibil_score = st.number_input("Pontuação CIBIL")
residential_assets_value = st.number_input("Valor dos ativos residenciais")
commercial_assets_value = st.number_input("Valor dos ativos comerciais")
luxury_assets_value = st.number_input("Valor dos ativos de luxo")
bank_asset_value = st.number_input("Valor do ativo bancário")

# Transformações categóricas para numéricas (como no LabelEncoder original)
education = 1 if education == "Graduado" else 0
self_employed = 1 if self_employed == "Sim" else 0

# Cria o array de entrada
input_data = np.array([[
    no_of_dependents, education, self_employed, income_annum, loan_amount,
    loan_term, cibil_score, residential_assets_value,
    commercial_assets_value, luxury_assets_value, bank_asset_value
]])

# Aplica o scaler
input_scaled = scaler.transform(input_data)

# Predição
if st.button("Verificar Aprovação"):
    prediction = model.predict(input_scaled)
    if prediction[0] == 1:
        st.success("✅ Empréstimo Aprovado!")
    else:
        st.error("❌ Empréstimo Não Aprovado.")