from statistika import spausdink_statistika as stat
from trynimas import trink_duomenis as trink
from paieska import ieskok
import pickle

pajamu_sarasas = []
islaidu_sarasas = []
try:
    with open("pajamu_islaidu_listas.txt", mode="rb") as file:
        pajamos_islaidos = pickle.load(file)
        pajamu_sarasas = pajamos_islaidos[0]
        islaidu_sarasas = pajamos_islaidos[1]
except FileNotFoundError:
    print("Failo dar nėra")

while True:
    print(""" Pasirinkite norimą veiksmą:
    1 - Įvesti pajamas
    2 - Įvesti išlaidas
    3 - Atspausdinti pajamas
    4 - Atspausdinti išlaidas
    5 - Rodyti statistiką
    6 - Duomenų trynimas
    7 - Duomenų paieška
    q - Išeiti iš programos
    """)
    pasirinkimas = input("> ")
    if pasirinkimas == "q":
        break

    if pasirinkimas == "1":
        print("Pajamų įvedimas")
        pajamu_data = input("Įveskite pajamų gavimo datą: ")
        pajamu_saltinis = input("Įveskite gautų pajamų šaltinį: ")
        pajamu_suma = int(input("Įveskite gautų pajamų sumą: "))
        pajamos = [pajamu_data, pajamu_saltinis, pajamu_suma]
        pajamu_sarasas.append(pajamos)
        input("")

    elif pasirinkimas == "2":
        print("Išlaidų įvedimas")
        islaidu_data = input("Įveskite patirtų išlaidų datą: ")
        islaidu_saltinis = input("Įveskite išlaidų šaltinį: ")
        islaidu_suma = int(input("Įveskite išlaidų sumą: "))
        islaidos = [islaidu_data, islaidu_saltinis, islaidu_suma]
        islaidu_sarasas.append(islaidos)
        input("")

    elif pasirinkimas == "3":
        print("Gautos pajamos")
        for pajamu_data, pajamu_saltinis, pajamu_suma in pajamu_sarasas:
            print(f"Pajamos gautos: {pajamu_data} | Pajamų šaltinis: {pajamu_saltinis} | Pajamų suma: {pajamu_suma}")
        input("")

    elif pasirinkimas == "4":
        print("Patirtos išlaidos")
        for islaidu_data, islaidu_saltinis, islaidu_suma in islaidu_sarasas:
            print(
                f"Išlaidos patirtos: {islaidu_data} | Išlaidų šaltinis: {islaidu_saltinis} | Išlaidų suma: {islaidu_suma}")
        input("")

    elif pasirinkimas == "5":
        stat(pajamu_sarasas, islaidu_sarasas)
        input("")
    elif pasirinkimas == "6":
        trink(pajamu_sarasas, islaidu_sarasas)
    elif pasirinkimas == "7":
        ieskok(pajamu_sarasas, islaidu_sarasas)
        input("")
    else:
        print("Prašome pasirinkti vieną iš aukščiau nurodytų funkcijų!")

pajamos_islaidos = [pajamu_sarasas, islaidu_sarasas]

with open("pajamu_islaidu_listas.txt", mode="wb") as file:
    # noinspection PyTypeChecker
    pickle.dump(pajamos_islaidos, file)
