
import pandas as pd
import numpy as np

excel = 'data_preprocessing/datasets/netflix_originals.csv'

df_netflix_2019 = pd.read_csv(excel)
#tipos de datos en cada una de las columnas 
df_netflix_2019.dtypes

#filas y columnas de la tabla
shape = df_netflix_2019.shape

#valores nulos
null = df_netflix_2019.isnull().sum()

null.sort_values(ascending=False)

for column in df_netflix_2019.columns:
    percetage = df_netflix_2019[column].isnull().mean()
    print(f'{column}: {round(percetage*100, 2)}%')


print("---------------------------")

no_runtime = df_netflix_2019[df_netflix_2019['runtime'].isnull()].index
df_netflix_2019.drop(no_runtime,axis=0)

df_netflix_2019[~df_netflix_2019['runtime'].isnull()]





for column in df_netflix_2019.columns:
    percetage = df_netflix_2019[column].isnull().mean()
    print(f'{column}: {round(percetage*100, 2)}%')
