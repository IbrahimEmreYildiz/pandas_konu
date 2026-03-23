import pandas as pd
import numpy as np


# personeller = {
#     'Worker': ['Ahmet Yilmaz', 'Can Ertürk', 'Hasan Korkmaz', 'Cenk Saymaz', 'Ali Turan', 'Riza Ertürk', 'Mustafa Can'],
#     'Department': ['İnsan Kaynaklari', 'Bilgi İşlem', None, 'İnsan Kaynaklari', 'Bilgi İşlem', 'Muhasebe', 'Bilgi İşlem'],
#     'Age': [30, 25, 45, 50, 23, 34, 42],
#     'Place': [None, 'Tuzla', 'Maltepe', 'Tuzla', 'Kadiköy', 'Tuzla', 'Maltepe'],
#     'Salary': [5000, 3000, None, 3500, None, 6500, None]
# }   

data= np.random.randint(10,100,15).reshape(5,3)
df=pd.DataFrame(data,index=['a','c','e','f','h'] ,columns=["Column1", "Column2", "Column3"])
df= df.reindex(['a','b','c','d','e','f','g','h']) # Yeniden indexleme 
result= df
result= df.drop(['a','b'], axis=0) # drop() silme işlemi için kullanılır axis= 0 satır axis=1 sütun
# isnull() NaN olan kısımları bulmaya yarar

result= df.isnull() # buna sum() eklersek null sayısını buluruz
result= df.notnull()
result= df.isnull().sum()
result= df["Column1"].isnull().sum()
newColumn= [np.nan, 30, np.nan, 51, np.nan,10, np.nan, 41] # nan değeri oluşturur
df["Column4"]=newColumn
# result= df.dropna() #içerisinde nan olan satırları getirmez.
# result= df.dropna(axis=1) # Sütuna göre bakar default değer axis= 0 dır
# result=df.dropna(how="any") # Herhangi bir nan değeri varsa o satırı getirmez how bir parametre
# result=df.dropna(how="all") # Satırın tamamı nan ise karşımıza gelmez 1 tane falan olursa yine gelir
result= df.dropna(subset=["Column3", "Column4"], how="any") # Sadece column3 ve column4 ye bakar ama yazdırırken hepsini yazdırır sadece 3 ve 4 de filtreleme yapar
result= df.dropna(thresh=2)# 2 tane normal veri varsa okey
result= df.dropna(thresh=4)# 4 tane normal veri varsa okey
result= df.fillna(value="no input")
toplam= df.sum() #column toplamını ayrı ayrı verir
toplam1= df.sum().sum() # tamamının toplamını verir
boyut= df.size# kaç elemanlı olduğunu verir
isnull_sum=df.isnull().sum()# columnlardakini ayrı ayrı verir
isnull_sum_all=df.isnull().sum().sum() # Tamamının sayısını verir

def ortalama(df):
    toplam= df.sum().sum()
    adet= df.size- df.isnull().sum().sum()
    return toplam/adet


result= df.fillna(value=ortalama(df))
print(result.round(2))

