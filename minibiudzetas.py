from statistika import spausdink_statistika as stat
from trynimas import trink_duomenis as trink
import pickle
pajamu_sarasas = []
islaidu_sarasas = []
try:
    with open("pajamu_islaidu_listas.txt", mode="rb") as file:
        pajamos_islaidos = pickle.load(file)
        pajamu_sarasas = pajamos_islaidos[0]
        islaidu_sarasas = pajamos_islaidos[1]
except FileNotFoundError:
    print("Failo dar nera")


while True:
    print(""" Pasirinkite norima veiksma:
    1 - Ivesti pajamas
    2 - Ivesti islaidas
    3 - Atspausdinti pajamas
    4 - Atspausdinti islaidas
    5 - Rodyti statistika
    6 - Duomenu trynimas
    q - iseiti is programos
    """)
    pasirinkimas = input("> ")
    if pasirinkimas == "q":
        break

    if pasirinkimas == "1":
        print("Pajamu ivedimas")
        pajamu_data = input("Iveskite pajamu gavimo data: ")
        pajamu_saltinis = input("Iveskite gautu pajamu saltini: ")
        pajamu_suma = int(input("Iveskite gautu pajamu suma: "))
        pajamos = [pajamu_data, pajamu_saltinis, pajamu_suma]
        pajamu_sarasas.append(pajamos)
        input("")

    elif pasirinkimas == "2":
        print("Islaidu ivedimas")
        islaidu_data = input("Iveskite patirtu islaidu data: ")
        islaidu_saltinis = input("Iveskite islaidu saltini: ")
        islaidu_suma = int(input("Iveskite islaidu suma: "))
        islaidos = [islaidu_data, islaidu_saltinis, islaidu_suma]
        islaidu_sarasas.append(islaidos)
        input("")

    elif pasirinkimas == "3":
        print("Gautos pajamos")
        for pajamu_data, pajamu_saltinis, pajamu_suma in pajamu_sarasas:
            print(f"Pajamos gautos: {pajamu_data} | Pajamu saltinis: {pajamu_saltinis} | Pajamu suma: {pajamu_suma}")
        input("")

    elif pasirinkimas == "4":
        print("Patirtos islaidos")
        for islaidu_data, islaidu_saltinis, islaidu_suma in islaidu_sarasas:
            print(
                f"Islaidos patirtos: {islaidu_data} | Islaidu saltinis: {islaidu_saltinis} | Islaidu suma: {islaidu_suma}")
        input("")

    elif pasirinkimas == "5":
        stat(pajamu_sarasas, islaidu_sarasas)
        input("")
    elif pasirinkimas == "6":
        print("""Pasirinkite, kuri sarasa norite pakoreguoti:
            Pajamu saraso korekcija - '1'
            Islaidu saraso korekcija - '2'
            """)
        saraso_pasirinkimas = input('')
        if saraso_pasirinkimas == "q":
            continue
        if saraso_pasirinkimas == "1":
            trink(pajamu_sarasas)
            input("")
        elif saraso_pasirinkimas == "2":
            trink(islaidu_sarasas)
            input("")
        else:
            print("Prasome pasirinkti viena is meniu nurodytu veiksmu: ")

    else:
        print("Prasome pasirinkti viena is auksciau nurodytu funkciju!")

pajamos_islaidos = [pajamu_sarasas, islaidu_sarasas]

with open("pajamu_islaidu_listas.txt", mode="wb") as file:
    # noinspection PyTypeChecker
    pickle.dump(pajamos_islaidos, file)
