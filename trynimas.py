def trink_duomenis(listas):
    for nr, (data, saltinis, suma) in enumerate(listas, start=1):
        print(f"{nr}. {data}|{saltinis}|{suma}")
    ivestis = int(input("Iveskite norimos pasalinti eilutes numeri: "))
    indeksas = ivestis - 1
    listas.pop(indeksas)
    return listas
