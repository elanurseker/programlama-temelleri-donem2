ders_notlari=[]
toplam=0
zayif_sayisi=0
for i in range (6):
    ders_notlari.append(int(input("ders notunuzu girin:")))
for ders_notlari in ders_notlari:
    toplam=toplam+ders_notlari
    if ders_notlari<50:
        zayif_sayisi=zayif_sayisi+1
ortalama=toplam/6
print("ders notualının ortalaması",ortalama)
print("öğrencinin zayıf sayısı", zayif_sayisi)