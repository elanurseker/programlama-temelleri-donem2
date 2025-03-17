adet=int(input("ürününüzün adedini girin:"))
birim_fiyati=int(input("ürünün biri fiyatını girin"))
toplam=adet*birim_fiyati
if toplam>=3000:
    toplam=toplam*0.20
    print("ürünün tutarı:",toplam)
else:
    toplam=toplam-100
    print("ürünlerin tutarı:", toplam)