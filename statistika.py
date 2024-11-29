# statistika:
# bendra pajamu suma
# bendra islaidu suma
#
# pameginti iskirstyti menesiais ir metais

def statistika(pajamu_listas, islaidu_listas):
    visos_pajamos = 0
    visos_islaidos = 0
    for pajamu_data, pajamu_saltinis, pajamu_suma in pajamu_listas:
        visos_pajamos += pajamu_suma
    for islaidu_data, islaidu_saltinis, islaidu_suma in islaidu_listas:
        visos_islaidos += islaidu_suma
    print(f"Bendra pajamu suma: {visos_pajamos}")
    print(f"Bendra islaidu suma: {visos_islaidos}")