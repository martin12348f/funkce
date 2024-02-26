def obvod(a,b,c):
    vysledek = a+b+c
    return  vysledek

def obsah(a,v):
    vysledek = 1/2*a*v
    return  vysledek

promena1 = int(input("zadej promenou 1: "))
promena2 = int(input("zadej promenou 2: "))
print("pro vypocet obvodu zadej 1")
print("pro vypocet obsahu zadej 2")
volba = input("zadejte vasi volbu")

if volba == "1":
    vysledek = obvod(promena1)
    print("vysledek je: ", vysledek)

elif volba == "2":
    vysledek = obsah(promena2)
    print("vysledek je: ", vysledek)

else:
    print("zadna voloba")



