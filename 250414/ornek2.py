park_sure=int(input("Kaç dakika kalacaksınız:"))
if park_sure <=60:
    print("ucret:5TL")
elif park_sure <=300:
    print("Ücret:",(park_sure/60)*4)
else:
    print("ücret:"(park_sure/60)*3)