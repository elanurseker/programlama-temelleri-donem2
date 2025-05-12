toplam=0
liste=[]
for i in range(8):
    liste.append(int(input("bir sayı girin:")))
for sayi in liste:
    if sayi%2==0:
        toplam=toplam+sayi
print("çift sayıların toplamı:",toplam)