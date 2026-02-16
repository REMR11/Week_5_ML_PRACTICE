#!/usr/bin/env python3
"""
Script para descargar el dataset Telco Customer Churn.
Fuente: IBM Sample Datasets / Kaggle
"""

import os
import sys

# Ruta del directorio data relativa al script
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
OUTPUT_PATH = os.path.join(DATA_DIR, "telco_churn.csv")


def download_from_url():
    """Descarga desde URL pública (IBM/Kaggle mirror)."""
    try:
        import urllib.request
        # URL del dataset IBM Telco Churn (versión pública)
        url = "https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/master/data/Telco-Customer-Churn.csv"
        os.makedirs(DATA_DIR, exist_ok=True)
        print(f"Descargando desde {url}...")
        urllib.request.urlretrieve(url, OUTPUT_PATH)
        print(f"Dataset guardado en: {OUTPUT_PATH}")
        return True
    except Exception as e:
        print(f"Error con URL IBM: {e}")
        return False


def create_sample_dataset():
    """
    Crea un dataset de muestra si la descarga falla.
    Incluye las características necesarias para los ejercicios.
    """
    import pandas as pd
    import numpy as np

    np.random.seed(42)
    n = 1000

    data = {
        "customerID": [f"0000-{i:04d}" for i in range(n)],
        "gender": np.random.choice(["Male", "Female"], n),
        "SeniorCitizen": np.random.choice([0, 1], n, p=[0.8, 0.2]),
        "Partner": np.random.choice(["Yes", "No"], n),
        "Dependents": np.random.choice(["Yes", "No"], n),
        "tenure": np.random.randint(0, 72, n),
        "PhoneService": np.random.choice(["Yes", "No"], n, p=[0.9, 0.1]),
        "MultipleLines": np.random.choice(["Yes", "No", "No phone service"], n),
        "InternetService": np.random.choice(["DSL", "Fiber optic", "No"], n),
        "OnlineSecurity": np.random.choice(["Yes", "No", "No internet service"], n),
        "OnlineBackup": np.random.choice(["Yes", "No", "No internet service"], n),
        "DeviceProtection": np.random.choice(["Yes", "No", "No internet service"], n),
        "TechSupport": np.random.choice(["Yes", "No", "No internet service"], n),
        "StreamingTV": np.random.choice(["Yes", "No", "No internet service"], n),
        "StreamingMovies": np.random.choice(["Yes", "No", "No internet service"], n),
        "Contract": np.random.choice(["Month-to-month", "One year", "Two year"], n),
        "PaperlessBilling": np.random.choice(["Yes", "No"], n),
        "PaymentMethod": np.random.choice(
            ["Electronic check", "Mailed check", "Bank transfer", "Credit card"], n
        ),
        "MonthlyCharges": np.round(np.random.uniform(20, 120, n), 2),
    }

    df = pd.DataFrame(data)

    # TotalCharges: tenure * MonthlyCharges + ruido (con algunos vacíos para missing values)
    df["TotalCharges"] = (df["tenure"] * df["MonthlyCharges"] * (0.9 + np.random.rand(n) * 0.2)).round(2)
    df.loc[df["tenure"] == 0, "TotalCharges"] = " "  # Missing no trivial
    df.loc[np.random.choice(df.index[df["tenure"] > 0], 5), "TotalCharges"] = " "

    # Churn: mayor probabilidad con contrato mensual y tenure bajo
    p_churn = 0.2 + 0.3 * (df["Contract"] == "Month-to-month").astype(int) - 0.01 * df["tenure"]
    p_churn = np.clip(p_churn, 0.05, 0.95)
    df["Churn"] = np.where(np.random.rand(n) < p_churn, "Yes", "No")

    os.makedirs(DATA_DIR, exist_ok=True)
    df.to_csv(OUTPUT_PATH, index=False)
    print(f"Dataset de muestra creado en: {OUTPUT_PATH}")
    print("(Usado porque la descarga externa no estuvo disponible)")


def main():
    if not download_from_url():
        print("Creando dataset de muestra alternativo...")
        create_sample_dataset()
    return 0


if __name__ == "__main__":
    sys.exit(main())
