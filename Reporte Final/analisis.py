import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

file = 'Car accidents/data.csv'

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

#Quitamos el valor atípico
df = df[df["Visibility(mi)"]<=15]

#Desplegar su histograma.
#df.hist(column="Visibility(mi)", color = "darkviolet")

#Desplegar el diagrama de cajas y bigotes.
#df.boxplot(column=["Visibility(mi)"], color = "purple", showmeans=True )



print("\nHumidity(%)")
print(df["Humidity(%)"])
print("Valores únicos:",df["Humidity(%)"].unique())
print("Valor máximo:",df["Humidity(%)"].max())
print("Valor mínimo:",df["Humidity(%)"].min())
print("Media:",df["Humidity(%)"].mean())
print("Mediana:",df["Humidity(%)"].median())
print("Desvición estándar:",df["Humidity(%)"].std())
#Desplegar su histograma
#df.hist(column="Humidity(%)", color = "maroon")
#Desplegar el diagrama de cajas y bigotes.
#df.boxplot(column=["Humidity(%)"], color = "maroon", showmeans=True )

#Despliega el mapa de calor de las correlaciones entre todas las variables numéricas. Escoge la visualización más adecuada y que aporte la mayor información posible para el análisis.
# plt.figure(figsize=(15, 5))
# df=df.select_dtypes('number')
# sns.heatmap(df.corr(), annot=True, cmap="gnuplot");



#----------------------------------------------------------------------------------------------------
#Utilizando scikitlearn calcula los centros del algoritmo k-means
# test = df[["Visibility(mi)","Humidity(%)"]]
# test = test.dropna(axis = 0, how = 'any')
# 
# kmeans = KMeans(n_clusters=4).fit(test)
# centroids = kmeans.cluster_centers_
# print("\nCentroides: ")
# print(centroids)
# 
# # Predicciones (cuál es la clase) de acuerdo a los centros calculados
# 
# cla = kmeans.predict(test)                   # obtiene las clases de los datos iniciales
# 
# df2=df[["Visibility(mi)","Humidity(%)"]].dropna(axis = 0, how = 'any')
# plt.scatter(df2["Visibility(mi)"],df2["Humidity(%)"],c=cla)
# for i in range(len(centroids)):
#     plt.scatter(centroids[i][0],centroids[i][1],marker="*",c="red")



plt.show()
