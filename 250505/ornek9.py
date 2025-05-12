ifade=(input("bir cümle/kelime girin:"))
adet=0
for aranan in ifade:
    if aranan=="a":
        adet=adet+1
print("bu ifade de toplam ",adet," adet a vardır")