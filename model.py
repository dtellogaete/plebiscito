# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 12:35:19 2020

@author: Daniel
"""

# Importar librerías

from twitterscraper import query_tweets
import datetime as dt 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 

# Importar dataset 
begin_date = dt.date(2020,2,13)
end_date = dt.date(2020,2,19)

limit = 1000000
lang = ['english', 'spanish']

tweets = query_tweets('#apruebo OR #rechazo', begindate = begin_date, enddate = end_date, limit = limit, lang = lang)
df = pd.DataFrame(t.__dict__ for t in tweets)


# Cast de las fechas
df['fecha']= df.iloc[:,5].values.astype('datetime64[D]')

# Transformo los hashtags en minúsculas
for i in range(0,len(df['hashtags'])):
    df['hashtags'][i]= [j.lower() for j in df['hashtags'][i]]      
   

# Crear columna de apruebo y rechazo
df['apruebo'] = 0
df['rechazo'] = 0

# Contar numero de twetts con rechazo y apruebo
for i in range(0,len(df['hashtags'])):
    if 'rechazo' in df['hashtags'][i]:
        df['apruebo'][i]=0
        df['rechazo'][i]=1
    if 'apruebo' in df['hashtags'][i]:
        df['apruebo'][i]=1
        df['rechazo'][i]=0
        

# Conteo y agrupación por #apruebo y #rechazo
df_group_apruebo = df[df['apruebo']==1]
df_group_rechazo = df[df['rechazo']==1]

        
df_group_apruebo = df_group_apruebo.groupby(['fecha']).count()
df_group_rechazo = df_group_rechazo.groupby(['fecha']).count()


# Visualización de datos
plt.plot(range(13,19), df_group_apruebo.iloc[:,1].values, color = "red", label= "#apruebo")
plt.plot(range(13,19), df_group_rechazo.iloc[:,1].values, color = "blue", label ="#rechazo")
plt.title("Twetts con #apruebo y #rechazo")
plt.xlabel('Día de Febrero')
plt.ylabel('Tweets')
plt.legend(loc="upper left")
plt.tight_layout()
plt.show()

















    

