import pandas as pd
from numpy.random import randn


df = pd.DataFrame(randn(3,3), index=['A', 'B', 'C'], columns=["Column1", "Column2","Column3"])

result = df

print(result)

print(result[["Column1","Column2"]])

result=df.loc["B","Column3"] # loc kullanırken row istersen direkt string olarak yazabiliriz ama column görüntülemek istersen row kısmına : koymalıyız ki tüm rowları göster demek için ve bunu liste paranteziyle yaparız çünkü indeksleme vardır.
# Eğer belirli bir aralıktaki column'ları istersem de şu şekilde yazmalıyım
result = df.loc[:, "Column1":"Column2"] #Column1 ve 2 yi getirir sadece
# Satır için de durum aynı
result= df.loc["A":"B",:"Column2"] # Başlangıçtan 2. column dahil olmak üzere A dan B'ye sınırlar dahil şekilde yazdırılır.


# Column ekleme

df["Column4"] = pd.Series(randn(3),['A','B','C'])
df["Column5"]= df["Column1"] + df["Column3"]
df.drop(['Column5'], axis=1, inplace=True)# inplace true yaparsak direkt df üstünde kalıcı değişiklik yapar yoksa geçici olarak değiştirir axis 1 ise sütun 0 sa satır
result = df
print(result)

