ders_not=[]
toplam=0
for i in range (6):
    ders_not.append(int(input("ders notlarını girin:")))
for sayi in ders_not:
    toplam=toplam+sayi
ort=ders_not/6
print("ortalamanız",ort)