from itertools import count
import pandas as pd
import numpy as np

excel_1 = ('excel_1.csv')
excel_2 = ('excel_2.csv')

df_excel_1 = pd.read_csv(excel_1)
df_excel_2 = pd.read_csv(excel_2)



df_excel_1 = df_excel_1.set_index('id')
df_excel_2 = df_excel_2.set_index('id')

description = df_excel_1.describe()
type = df_excel_1.dtypes



df_pivot = df_excel_1.pivot_table(index='Lote', values =['Pale'], aggfunc='mean')

values_1= df_excel_1['Lote'].value_counts()
values_2= df_excel_2['Lote'].value_counts()

#print (values_1.sort_values(ascending=False))
#print ("----------------------------------")
#print (values_2.sort_values(ascending=False))


length_1 = len(df_excel_1.index)
length_2 = len(df_excel_2.index)





    


