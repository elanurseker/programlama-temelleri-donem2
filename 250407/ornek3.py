kadi=input("kullanıcı adını girin:")
karakter_sayi=len(kadi)
if karakter_sayi==0:
    print("kullanıcı adı boş geçilmez")
elif karakte_sayi>0 and karakter_sayi<3:
    print("kullanıcı adı çok kısa0")
elif karakter_sayi>=3 and karakter_sayi<9:
    print("kullanıcı adı uygun")
else:
    print("kullanıcı adı çok uzun")