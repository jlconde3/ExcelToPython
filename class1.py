import numpy as np  
import pandas as pd
import matplotlib.pyplot as plt

df_excel = pd.read_csv('data_preprocessing/datasets/StudentsPerformance_id.csv')

#Descripción general de la tabla
df_excel.describe()

#Para ver media por columna
df_excel['math score'].mean()

#Media aritmética de una fila 
df_excel['average'] = (df_excel['math score']+df_excel['reading score']+df_excel['writing score'])/3

#Contar valores en columnas
df_excel['gender'].value_counts()

#Sustituir el if pr np.where
df_excel['pass/fail'] = np.where (df_excel['average']> 70, 'Pass', 'Fail')

#Según valor de la columna 'average' asignar un valor A a F usando np.select
conditions = [
    (df_excel['average']>=90),
    (df_excel['average']>=80)&(df_excel['average']<90),
    (df_excel['average']>=70)&(df_excel['average']<80),
    (df_excel['average']>=60)&(df_excel['average']<70),
    (df_excel['average']>=50)&(df_excel['average']<60),
    (df_excel['average']<50),
]
values = ['A','B','C','D','E','F']

df_excel['grades'] = np.select(conditions,values)

#Aplicar una condición determinada para obtener un df determinado
df_female = df_excel[df_excel['gender']=='female']

#Aplicar varias condiciones para obtener un df determinado 
df_sumifs = df_excel[(df_excel['race/ethnicity']=='group B')&(df_excel['gender']=='female')]

#Creamos una nueva columna que es la suma de la tres notas en el df sumifs y que se llama sumifs
df_sumifs = df_sumifs.assign(sumifs = df_sumifs['math score']+df_sumifs['reading score']+df_sumifs['writing score'])

#Transformar valores de una columna su primera letra a mayuscula
df_excel['gender'] = df_excel['gender'].str.title()

#Extraer valores de una columna
df_excel['group'] = df_excel['race/ethnicity'].str.extract (r' ([A-Z])')

#Filtrar por valores en blanco
df_excel['gender'].isnull()

#BuscarV en np
excel_1 = 'data_preprocessing/datasets/StudentsPerformance_id.csv'
excel_2 = 'data_preprocessing/datasets/LanguageScore.csv'

df_excel_1 = pd.read_csv(excel_1)
df_excel_2 = pd.read_csv(excel_2)

#Muestra información de una fila y una columna 
df_excel_1.loc[100 ,'math score']
df_excel_1.loc[df_excel_1['id']==100, 'math score']

#unir tablas pd.merge
df_excel_3 = pd.merge(df_excel_1, df_excel_2, on = 'id', how= 'left')

#unir tablas pd.concat
df_excel_3 = pd.concat([df_excel_1.set_index('id'),df_excel_2.set_index('id')], axis= 1)
df_excel_3['language score'].fillna('0', inplace= True)

df_0 = df_excel_3[df_excel_3['language score'] == '0']

#tabla dinámica media por grupos étnicos
df_pivot = df_excel_3.pivot_table(index='race/ethnicity', values=['math score', 'writing score'], aggfunc='mean')

#representación gráfica
df_plot = df_pivot.reset_index()

print (df_plot)
plt.bar(df_plot['race/ethnicity'], df_plot['math score'])
plt.show()


