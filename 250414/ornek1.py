sayi1=int(input("sayı girin:"))
sayi2=int(input("sayı girin:"))
islem =input("işlem seçin (+,-,*,/):")
if islem=="+":
    sonuc=sayi1+sayi2
    print(sonuc)
elif islem =="-":
    sonuc=sayi1-sayi2
    print(sonuc)
elif islem== "*":
    sonuc=sayi1*sayi2
    print(sonuc)
elif islem== "/":
    sonuc=sayi1/sayi2
    print(sonuc)
else:
    print("yanlış işlem girdiniz")