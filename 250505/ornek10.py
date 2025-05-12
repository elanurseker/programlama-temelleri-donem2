toplam=0
liste=[]
for i in range (5):
    liste.append(int(input("bir sayı girin:")))
for sayi in liste:
    toplam=toplam+sayi
print("toplam:",toplam)