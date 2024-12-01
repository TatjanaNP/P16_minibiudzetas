# statistika:

# sugrupuoti pagal islaidu pobudi

# pameginti iskirstyti menesiais ir metais

def spausdink_statistika(pajamu_listas, islaidu_listas):
    visos_pajamos = 0
    visos_islaidos = 0
    didziausios_pajamos = 0
    didziausios_islaidos = 0
    max_pajamos = []
    max_islaidos = []
    for pajamu_data, pajamu_saltinis, pajamu_suma in pajamu_listas:
        visos_pajamos += pajamu_suma
        if pajamu_suma > didziausios_pajamos:
            didziausios_pajamos = pajamu_suma
            max_pajamos = [pajamu_data, pajamu_saltinis, pajamu_suma]
    for islaidu_data, islaidu_saltinis, islaidu_suma in islaidu_listas:
        visos_islaidos += islaidu_suma
        if islaidu_suma > didziausios_islaidos:
            didziausios_islaidos = islaidu_suma
            max_islaidos = [islaidu_data, islaidu_saltinis, islaidu_suma]

    print(f"Bendra pajamų suma: {visos_pajamos}")
    print(f"Bendra išlaidų suma: {visos_islaidos}")
    print(f"Didžiausios gautos pajamos:", end=" ")
    for elem in max_pajamos:
        print(elem, end=" ")
    print("")
    print(f"Didžiausios patirtos išlaidos:", end=" ")
    for elem in max_islaidos:
        print(elem, end=" ")