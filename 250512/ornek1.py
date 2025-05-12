toplam=0
liste=[]
for i in range (7):
    liste. append(int(input("Bir sayı girin:")))
for sayi in liste:
    toplam=toplam+sayi
print("Toplam:",toplam)
if toplam%2==0:
    print("sayınız çiftdir.")
else:
    print("sayınız tektir.")