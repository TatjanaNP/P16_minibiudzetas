def ieskok(listas_pajamu, listas_islaidu):
    # print("""Pasirinkite paieskos metoda:
    # 1 - Pagal islaidu/pajamu data
    # 2 - Pagal islaidu/pajamu paskirti
    # 3 - pagal islaidu/pajamu suma""")

    elementas_paieskai = input("Iveskite paieskos elementa: ")

    for listas in listas_pajamu:
        for elem in listas:
            if str(elem) == elementas_paieskai:
                print(listas)
    for listas in listas_islaidu:
        for elem in listas:
            if str(elem) == elementas_paieskai:
                print(listas)