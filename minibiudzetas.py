from statistika import statistika as stat
import pickle

# try:
#     with open("pajamu_islaidu_listas.txt", mode="r") as file:
#         pajamos_islaidos = pickle.load(file)
# except FileNotFoundError:
#     print("Failo dar nera")
#

pajamu_sarasas = []
islaidu_sarasas = []
while True:
    print(""" Pasirinkite norima veiksma:
    1 - Ivesti pajamas
    2 - Ivesti islaidas
    3 - Atspausdinti pajamas
    4 - Atspausdinti islaidas
    5 - Rodyti statistika
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

    else:
        print("Prasome pasirinkti viena is auksciau nurodytu funkciju!")
finansai = [pajamu_sarasas, islaidu_sarasas]

with open("pajamu_islaidu_listas.txt", mode="wb") as file:
    # noinspection PyTypeChecker
    pickle.dump(finansai, file)

