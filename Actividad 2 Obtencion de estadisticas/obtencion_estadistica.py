import pandas as pd

file = 'Car accidents/data.csv'

#Cargar los datos
df = pd.read_csv(file)

#Mostrar el número de variables y el número de registros
print("Número de variables:",df.shape[1],"\nNúmero de registros:",df.shape[0])

#Mostrar el nombre de las columnas
variables=""
for variable in df.columns:
    variables = variables + variable + ', '
print("\nVariables:",variables)    

#Mostrar los tipos de datos
print("\n", df.dtypes)

#Selecciones dos columnas que al momento parezcan interesantes. Para ellas:
#Mostrar los valores únicos
#Mostrar los valores máximos y mínimos
#Mostrar la media, la mediana y la desviación estándar.
print("\nVisibility(mi)")
print(df["Visibility(mi)"])
print("Valores únicos:",df["Visibility(mi)"].unique())
print("Valor máximo:",df["Visibility(mi)"].max())
print("Valor mínimo:",df["Visibility(mi)"].min())
print("Media:",df["Visibility(mi)"].mean())
print("Mediana:",df["Visibility(mi)"].median())
print("Desvición estándar:",df["Visibility(mi)"].std())

print("\nPressure(in)")
print(df["Pressure(in)"])
print("Valores únicos:",df["Pressure(in)"].unique())
print("Valor máximo:",df["Pressure(in)"].max())
print("Valor mínimo:",df["Pressure(in)"].min())
print("Media:",df["Pressure(in)"].mean())
print("Mediana:",df["Pressure(in)"].median())
print("Desvición estándar:",df["Pressure(in)"].std())
