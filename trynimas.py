def trink_duomenis(pajamu_sarasas, islaidu_sarasas):
    while True:
        print("""Pasirinkite, kuri sarasa norite pakoreguoti:
            Pajamu saraso korekcija - '1'
            Islaidu saraso korekcija - '2'
            Baigti trynima - 'q'
            """)
        saraso_pasirinkimas = input('')
        if saraso_pasirinkimas == "q":
            break
        if saraso_pasirinkimas == "1":
            for nr, (data, saltinis, suma) in enumerate(pajamu_sarasas, start=1):
                print(f"{nr}. {data}|{saltinis}|{suma}")
            ivestis = int(input("Iveskite norimos pasalinti eilutes numeri: "))
            indeksas = ivestis - 1
            pajamu_sarasas.pop(indeksas)
            input("")
        elif saraso_pasirinkimas == "2":
            for nr, (data, saltinis, suma) in enumerate(islaidu_sarasas, start=1):
                print(f"{nr}. {data}|{saltinis}|{suma}")
            ivestis = int(input("Iveskite norimos pasalinti eilutes numeri: "))
            indeksas = ivestis - 1
            islaidu_sarasas.pop(indeksas)
        else:
            print("Prasome pasirinkti viena is meniu nurodytu veiksmu: ")

    return pajamu_sarasas, islaidu_sarasas
