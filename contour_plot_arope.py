import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar datos
df = pd.read_csv("datos_arope.csv")

# Mapear sexo a texto
df["Sexo"] = df["Sexo"].map({0: "Hombres", 1: "Mujeres"})

# Pivot para grid de contour
pivot_df = df.pivot(index="Edad_media", columns="Sexo", values="AROPE_2025")

# Crear contour plot
plt.figure(figsize=(8,6))
sns.heatmap(pivot_df, annot=True, cmap="YlGnBu")
plt.title("Riesgo de pobreza (AROPE 2025) por edad y sexo")
plt.xlabel("Sexo")
plt.ylabel("Edad media")
plt.tight_layout()
plt.show()
