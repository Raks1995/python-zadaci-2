pokusaji35 = 0
pokusaji3 = 0
pokusaji5 = 0

for x in range(1, 100):
    x = int(input("Unesi broj od 1 do 100: "))
    if x % 3 == 0 and x % 5 == 0:
        pokusaji35 += 1
    elif x % 5 == 0:
        pokusaji5 += 1
    elif x % 3 == 0:
        pokusaji3 += 1
    elif x % 5 != 0 or x % 3 != 0:
        print("Unesena su {0} broja djeljiva sa 3 i 5".format(pokusaji35))
        print("Unesena su {0} broja djeljiva sa 5".format(pokusaji5))
        print("Unesena su {0} broja djeljiva sa 3".format(pokusaji3))
        break



