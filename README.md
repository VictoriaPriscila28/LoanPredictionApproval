# 🧠 Sistema de Predição de Aprovação de Empréstimos

Este projeto utiliza aprendizado de máquina para prever se um empréstimo será aprovado ou não, com base em dados históricos.

## 📂 Estrutura do Projeto

loan-prediction/ │ ├── loan_approval_dataset.csv ├── Loan_Prediction_Models.ipynb ├── streamlit_app.py ├── best_loan_model.pkl ├── scaler.pkl ├── requirements.txt └── README.md


## 🚀 Tecnologias Utilizadas

- Python
- Pandas, NumPy, Scikit-learn
- Streamlit
- MongoDB (Atlas)
- Matplotlib / Seaborn

## 📊 Modelos Treinados

- Random Forest 🌟 (melhor modelo com 98.24% de acurácia)
- Logistic Regression
- K-Nearest Neighbors (KNN)
- Decision Tree

## ⚙️ Como Executar

1. Clone este repositório.
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt


## 🚀 Tecnologias Utilizadas

- Python
- Pandas, NumPy, Scikit-learn
- Streamlit
- MongoDB (Atlas)
- Matplotlib / Seaborn

## 📊 Modelos Treinados

- Random Forest 🌟 (melhor modelo com 98.24% de acurácia)
- Logistic Regression
- K-Nearest Neighbors (KNN)
- Decision Tree

## ⚙️ Como Executar

1. Clone este repositório.
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
3. Rode o notebook Loan_Prediction_Models.ipynb para treinar/testar modelos.

4. Rode o app com Streamlit:
streamlit run streamlit_app.py

## 📊 Dashboard

O dashboard em Streamlit permite:

- ✅ Inserir dados manualmente e obter predição de aprovação.
- 📈 Visualizar estatísticas e gráficos com base nas predições armazenadas no MongoDB.

## 🧪 Resultados dos Modelos

| Modelo              | Acurácia Média |
|---------------------|----------------|
| Random Forest       | 0.9824         |
| Logistic Regression | 0.9179         |
| KNN                 | 0.8972         |
| Decision Tree       | 0.9785         |

## 💾 Armazenamento

As predições são armazenadas em tempo real no **MongoDB Atlas**, permitindo análises futuras.
