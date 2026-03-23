import pandas as pd
import openpyxl



# Kaggle'dan indirdiğim veri setini okuma dosya json ise pd.read_json('Dosya adı') Türkçe karakterler içeriyorsa encoding= 'utf-8' yaparsan karakterler düzelir
df = pd.read_csv('videos-stats.csv')
#print(df)
dff= pd.read_excel('notlar.xlsx')
print(dff)

df2= pd.read_sql_query('file name') # Bu kısım database dosyalarını okumak için kullanılır.

