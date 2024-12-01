def ieskok(listas_pajamu, listas_islaidu):
    # print("""Pasirinkite paieskos metoda:
    # 1 - Pagal islaidu/pajamu data
    # 2 - Pagal islaidu/pajamu paskirti
    # 3 - pagal islaidu/pajamu suma""")
    while True:
        elementas_paieskai = input("Įveskite paieškos elementą arba išeikite is programos(q): ").lower()
        if elementas_paieskai == "q":
            break
        for data, saltinis, suma in listas_pajamu:
            if data.lower() == elementas_paieskai.lower() or saltinis.lower() == elementas_paieskai or suma ==elementas_paieskai:
                print(f"{data} | {saltinis} | {suma}")
        for data, saltinis, suma in listas_islaidu:
            if data.lower() == elementas_paieskai.lower() or saltinis.lower() == elementas_paieskai or suma == elementas_paieskai:
                print(f"{data} | {saltinis} | {suma}")
