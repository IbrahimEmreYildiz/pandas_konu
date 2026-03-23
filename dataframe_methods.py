import pandas as pd
import numpy as np


data = {
    "Column1": [1, 2, 3, 4, 5, 6],
    "Column2": [10, 20, 20, 13, 45, 25],
    "Column3": ["abc", "bca", "ade", "cba", "dea", "dba"]
}

df=pd.DataFrame(data)
result=df

result= df["Column2"].unique() # Column2'deki eşsiz verileri gösterir yani set() gibi bir şey olur
result= df["Column2"].nunique() # Eşsiz elemanların sayısını gösterir
result= df["Column2"].value_counts() # Hangi karakterden kaç tane var onu gösterir
def kareal(x):
    return x**2


kareal2= lambda x: x**2 # lambda olarak direkt apply'ın içine de yazabiliriz
result= df["Column2"].apply(kareal2) # apply() içine yazdığımız fonksiyonu o column'un tek tek tüm elemanlarına uygular
df["Column4"]= df["Column3"].apply(len) # apply'ın içine python methodlarını da verebiliriz
result=df.index #indexler hakkında bilgi verir --> RangeIndex(start=0, stop=6, step=1)
result= len(df.index) # Satır sayısı
result= df.sort_values("Column2")["Column2"] # Column2 'yi sıralı şekilde yazdırır
result= df.sort_values("Column3")["Column3"] # Alfabetik sıraya koyar
result= df.sort_values("Column3",ascending=False)["Column3"] #Böyle yaparsak sıralamayı tersten yapar ascending alfabetik olsun mu sorusudur

data = {
    "Ay": ["Mayıs", "Haziran", "Nisan", "Mayıs", "Haziran", "Nisan", "Mayıs", "Haziran", "Nisan"],
    "Kategori": ["Elektronik", "Elektronik", "Elektronik", "Kitap", "Kitap", "Kitap", "Giyim", "Giyim", "Giyim"],
    "Gelir": [20, 30, 15, 14, 32, 42, 12, 36, 52]
}

df=pd.DataFrame(data)

result= df

result= df.pivot_table(index="Ay", columns="Kategori", values="Gelir")




print(result)
