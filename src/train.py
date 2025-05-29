import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
import pickle

# Cargar datos
df = pd.read_csv("data/dataset.csv")

X = df.drop("target", axis=1)
y = df["target"]

# Preprocesamiento
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Entrenamiento
model = LogisticRegression()
model.fit(X_scaled, y)

# Guardar modelo y transformador
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("transformer.pkl", "wb") as f:
    pickle.dump(scaler, f)
