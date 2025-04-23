
import streamlit as st
import numpy as np
import pickle
from datetime import datetime
from pymongo import MongoClient
import pandas as pd
import plotly.express as px

# Carrega modelo e scaler
model = pickle.load(open("best_loan_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

#Mongo
client = MongoClient("mongodb+srv://admin:YNgicguYy7MfdfLR@cluster0.evsh2.mongodb.net/")
db = client["db_docker"]
collection = db["db_docker_financeiro"]


# Página
st.title("🔍 Preditor de Aprovação de Empréstimo")

# Inputs
no_of_dependents = st.number_input("Número de dependentes", min_value=0)
education = st.selectbox("Educação", ["Graduado", "Não graduado"])
self_employed = st.selectbox("Autônomo", ["Sim", "Não"])
income_annum = st.number_input("Renda anual")
loan_amount = st.number_input("Valor do empréstimo")
loan_term = st.number_input("Prazo (meses)")
cibil_score = st.number_input("Pontuação CIBIL")
residential_assets_value = st.number_input("Valor ativos residenciais")
commercial_assets_value = st.number_input("Valor ativos comerciais")
luxury_assets_value = st.number_input("Valor ativos de luxo")
bank_asset_value = st.number_input("Valor ativo bancário")

# Conversões
education = 1 if education == "Graduado" else 0
self_employed = 1 if self_employed == "Sim" else 0

input_data = np.array([[
    no_of_dependents, education, self_employed, income_annum, loan_amount,
    loan_term, cibil_score, residential_assets_value,
    commercial_assets_value, luxury_assets_value, bank_asset_value
]])

input_scaled = scaler.transform(input_data)

# Predição
if st.button("Verificar Aprovação"):
    prediction = model.predict(input_scaled)
    result = "Aprovado" if prediction[0] == 1 else "Reprovado"

    # Exibe o resultado
    st.subheader(f"Resultado: {result}")

    # Armazena no MongoDB
    collection.insert_one({
        "inputs": input_data.tolist()[0],
        "prediction": int(prediction[0]),
        "timestamp": datetime.now()
    })

# Dashboard
st.header("📊 Dashboard de Predições")

data = pd.DataFrame(list(collection.find()))
if not data.empty:
    st.write("### Total de predições:", len(data))

    data["prediction"] = data["prediction"].replace({1: "Aprovado", 0: "Reprovado"})
    st.plotly_chart(px.pie(data, names='prediction', title='Distribuição das Predições'))

    st.plotly_chart(px.histogram(data, x=data["inputs"].apply(lambda x: x[3]), title="Distribuição da Renda Anual",
                                 labels={"x": "Renda Anual"}))
