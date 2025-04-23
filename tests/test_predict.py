# tests/test_predict.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from predict import fazer_predicao


def test_predicao_simples():
    entrada = {
        "income_annum": 60000,
        "loan_amount": 2000,
        "loan_term": 12,
        "cibil_score": 750,
        "no_of_dependents": 1,
        "education": "Graduate",
        "self_employed": "No"
    }

    resultado = fazer_predicao(entrada)

    assert resultado in [0, 1], "A predição deve ser 0 ou 1"

