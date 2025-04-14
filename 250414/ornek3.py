kenar1=int(input("kenar uzunluğunu girin"))
kenar2=int(input("kenar uzunluğunu girin"))
kenar3=int(input("kenar uzunluğunu girin"))
if kenar1== kenar2 and kenar2==kenar3:
    print("bu bir eşkenar üçgendir")
elif kenar1==kenar2 or kenar2==kenar3 or kenar3==kenar1:
    print("bu bir ikiz kenar üçgendir")
else:
    print("bu bir çeşit kenar üçgendir")