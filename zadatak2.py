print("Unesi dva broja (1-9) da dobiješ parne brojeve koje ta 2 broja čine.")
x = (input("Broj 1: "))
y = (input("Broj 2: "))
z = (x + y)
w = (y + x)

if 10 > (int(x) and int(y)) > 0:
    if int(x) % 2 == 0 and int(y) % 2 == 0:
        print("Parni brojevi stvoreni od znamenaka {0} i {1} su: {2} i {3}".format(x, y, z, w))
    elif int(x) % 2 == 0 and int(y) % 2 != 0:
        print("Parni brojevi stvoreni od znamenaka {0} i {1} su: {2}".format(x, y, w))
    elif int(x) % 2 != 0 and int(y) % 2 == 0:
        print("Parni brojevi stvoreni od znamenaka {0} i {1} su: {2}".format(x, y, z))
    elif int(x) % 2 != 0 and int(y) % 2 != 0:
        print("Nema parnih brojeva")
else:
    print("Krivi unos. Unesi broj od 1 do 9.")
