import pandas as pd
import numpy as np



# pandas seri oluşturma otomatik index verir 0 dan başlayarak
numbers=[5,10,15,20,25]
letters=[10,20,30,40,50]
dict={'a':5, 'b':6, 'c':7, 'd':8, 'e':9}
randomNumbers=np.random.randint(1,100,5)
pandas_series=pd.Series(numbers)
pandas_serisi=pd.Series(letters)
pandas_series=pd.Series(5, [1,2,3,4,5]) # Burada 5 'i 1 2 3 4 ve 5. indexlere koyar.
pandas_series=pd.Series(numbers, ['a','b','c','d','e']) #İlk yazılan üyeler ikinci yazılan index olarak geçer. Böyle indeks bilgisi versek de 0. eleman yine a yerine geçer 0'a ulaşsak da a ile aynı sonucu verir.
pandas_series=pd.Series(dict) # Dictionary yaptığımızda ise key index olur value yine value olarak kalır
pandas_serisi=pd.Series(randomNumbers) 
# Slicing numpy ile aynı
pandas_series=pd.Series(numbers) # burada istediğimiz indexleri verip değerlerine ulaşabiliriz
print(pandas_series[['a','c']]) # gibi , eğer olmayan index'i istersek NaN çıktısını verir bu da Not a Number anlamına gelir.
print(pandas_series.ndim) # numpy'dakileri de kullanabiliriz boyut sorgulama gibi.  
print(pandas_series.dtype)
print(pandas_series.shape)
print(pandas_series.sum())
print(pandas_series.max())
result= pandas_serisi % 2 ==0 # çift olup olmama kontrolü true false çıktısı verir
print(result)
print(pandas_serisi[result])# çift olanları yazdırır
# kısacası numpy'daki işlemlerin hepsi kullanılabilir.
# print(pandas_series + pandas_serisi)



#DATAFRAME -> 2 serinin toplanması sonucu oluşur

s1= pd.Series([0,3,9,11])
s2= pd.Series([3,6,7,8])

data= dict(apples=s1 , oranges=s2)

df= pd.DataFrame(data)

data=[["Ahmet",50],["Emre", 100], ["Kaan", 100],["Mehmet", 99]]

df=pd.DataFrame(data, index=[1,2,3,4], columns=["Name","Grade"])
df["Grade"]=df["Grade"].astype(float)
print(df)




