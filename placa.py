print("Ako imate 10 ili više godina staža dobit ćete povišicu!")
trenutna_placa = int(input("Unesi svoju trenutnu plaću:"))
godine_staza = int(input("Godine staža: "))

if godine_staza >= 10:
    nova_placa = trenutna_placa + trenutna_placa * (godine_staza / 100)
    print("Vaša plaća će od sad iznositi: " + str(nova_placa))
else:
    print("Uvjeti za povišicu nisu ispunjeni.")