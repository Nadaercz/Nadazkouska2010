# UKOL 1
cisla = [-5, -4, 0, 5, 0, 0,10, 15]
#a
for cislo in cisla:
    print(cisla)

#b
for cislo in cisla:
    print(cislo,-cislo)

#c
for cislo_vetsi_nez_o in cisla:
        if cislo_vetsi_nez_o>0:
            print(cislo_vetsi_nez_o)

#d
for cislo_vetsi_nez_o in cisla:
        if cislo_vetsi_nez_o<0:
            print(-cislo_vetsi_nez_o)
        else:
            print(cislo_vetsi_nez_o)
#UKOL 2
jmena = ['petr', 'pavel', 'jitka', '', 'jana']
for jmeno in jmena:
    if jmeno[0] == 'p':
        print('pako')
    else:
        print(jmeno)