urun1=int(input("Ürünün fiyatını gitin:"))
urun2=int(input("Ürünün fiyatını girin:"))
toplam=urun1+urun2
if toplam<=200:
    print("Ödenecek",toplam)
else:
    odeme=toplam*0,75
    print("Ödenecek miktar", odeme)
 