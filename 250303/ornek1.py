bagaj= int (input ("Toplam bagajı girin:" ))
if bagaj <=20:
    print("Herhangi bir ücret ödemenize gerek yok")
else:
    fark=bagaj-20
    print("Fazla bagaj için",10*fark,"TL ödemelisiniz")
print("İyi yolculuklar.")