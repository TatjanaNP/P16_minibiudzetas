def ieskok(listas_pajamu, listas_islaidu):
    # print("""Pasirinkite paieskos metoda:
    # 1 - Pagal islaidu/pajamu data
    # 2 - Pagal islaidu/pajamu paskirti
    # 3 - pagal islaidu/pajamu suma""")
    while True:
        elementas_paieskai = input("Įveskite paieškos elementą arba išeikite is programos(q): ").lower()
        if elementas_paieskai == "q":
            break
        for listas in listas_pajamu:
            for elem in listas:
                if str(elem).lower() == elementas_paieskai:
                    print(listas)
        for listas in listas_islaidu:
            for elem in listas:
                if str(elem).lower() == elementas_paieskai:
                    print(listas)
