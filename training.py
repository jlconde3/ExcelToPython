
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

P20NP239 = pd.read_excel('Horas Proyecto (Web) - Responsable_sl01htlw.xlsx',1)
P21NP216 = pd.read_excel('Horas Proyecto (Web) - Responsable_3qvswiui.xlsx',1)



P20NP239_horas = P20NP239.drop(columns=['T', 'Compañía', 'Imputador (T)','Resno','Resno (T)', 'Proyecto (T)', 'Fase (T)', 'Orden Trabajo (T)'])
P21NP216_horas = P21NP216.drop(columns=['T', 'Compañía', 'Imputador (T)','Resno','Resno (T)', 'Proyecto (T)', 'Fase (T)', 'Orden Trabajo (T)'])


#Horas por imputador
df_pivot = P20NP239_horas.pivot_table(index = 'Imputador', values ='Horas', columns = ['Fase'], aggfunc= np.sum)

#Horas por semana
df_pivot = P20NP239_horas.pivot_table(index = 'Periodo', values ='Horas', aggfunc= np.sum)



df_plot = df_pivot.reset_index()
df_plot['Horas'] = df_plot['Horas'].cumsum()

plt.bar(df_plot['Periodo'],df_plot['Horas'])
plt.show()













