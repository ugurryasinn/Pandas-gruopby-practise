import pandas

personeller = {
    'Çalışan': ['Ahmet Yılmaz','Can Ertürk','Hasan Korkmaz','Cenk Saymaz','Ali Turan','Rıza Ertürk','Mustafa Can'],
    'Departman': ['İnsan Kaynakları','Bilgi İşlem','Muhasebe','İnsan Kaynakları','Bilgi İşlem','Muhasebe','İnsan Kaynakları'],
    'Yaş': [30,25,45,50,23,34,42],
    'Semt': ['Kadıköy','Tuzla','Maltepe','Tuzla','Maltepe','Tuzla','Kadıköy'],
    'Maaş': [5000,3000,4000,3500,2750,6500,4500]

}

data=pandas.DataFrame(personeller)

""""
for name, group in data.groupby("Semt"):  #semte göre gruplandırarak tabloyu getirdi. semt kısmını değiştirerek genel tabloya ulaşabilirsin
    print(name)
    print(group)
"""
"""
for name,group in data.groupby("Departman"):
    print(f"{name}, {group}")
"""

result=data
result = data.groupby("Semt").get_group("Kadıköy") #semti kadıköy olan grubu getirir.
result = data.groupby("Departman").get_group("Muhasebe") #departmanı muhasebe olan grubu getirir.
result = data.groupby("Departman").sum() # her departmanın yaş ve maaşlarının toplamını verir. (type int veya float olanları işin içince katıyor)
result = data.groupby("Departman").mean() # her departmanın yaş ve maaşlarının ortalamasını verir.
result = data.groupby("Departman")["Maaş"].mean() #her departmanın sadece maaş ortalamalarını verir.
result = data.groupby("Semt")["Çalışan"].count() #hangi semtte kaç çalışan olduğunu verir.
result = data.groupby("Departman")["Yaş"].max() #her departmanda bulunan en yaşlının yaşını verir.
result = data.groupby("Departman")["Maaş"].max()["Muhasebe"] #muhasebe departmanında çalışan en yüksek maaşı getirir.

print(result)

