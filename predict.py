import pickle
import numpy as np
import joblib
import pandas as pd

pipeline = joblib.load('model/pipeline.pkl')  # salve o pipeline completo assim no treinamento

def fazer_predicao(entrada_dict):
    entrada_df = pd.DataFrame([entrada_dict])
    predicao = pipeline.predict(entrada_df)
    return int(predicao[0])


# Caminho para o modelo salvo (ajuste se necessário)
MODEL_PATH = "best_loan_model2.pkl"

def fazer_predicao(dados_input):
    """
    Recebe um dicionário com os dados de entrada (já padronizados) e retorna a predição do modelo.
    """
    # Converter dicionário para vetor numpy na ordem correta dos atributos
    atributos = ['income_annum', 'loan_amount', 'loan_term', 'cibil_score', 'no_of_dependents']
    vetor = np.array([[dados_input[atributo] for atributo in atributos]])

    # Carregar modelo
    with open(MODEL_PATH, 'rb') as file:
        modelo = pickle.load(file)

    # Fazer predição
    predicao = modelo.predict(vetor)

    return int(predicao[0])
