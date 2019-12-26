x = int(input("Pare: "))
kn50 = x // 50
kn20 = (x % 50) // 20
kn5 = ((x % 50) % 20) // 5
kn2 = (((x % 50) % 20) % 5) // 2
kn1 = ((((x % 50) % 20) % 5) % 2) // 1

if x > 0:
    print("Broj novčanica od 50 kn: " + str(kn50))
    if x > 0:
        print("Broj novčanica od 20 kn: " + str(kn20))
        if x > 0:
            print("Broj novčanica od 5 kn: " + str(kn5))
            if x > 0:
                print("Broj novčanica od 2 kn: " + str(kn2))
                if x > 0:
                    print("Broj novčanica od 1 kn: " + str(kn1))
else:
    print("Krivi unos")