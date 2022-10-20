absolvent_1 = ['Petr', 2017, 0.95, True]
absolvent_2 = ['Roman', 2017, 0.98, False]

#seznam_absolventru

#Slovník umožňuje pojmenovat hodnoty v nějaké datové struktuře tak, abychom pomocí těchto jmen mohli k hodnotám poté přistupovat. 
absolvent = {
    'jmeno': 'Petr',
    'prijmeni': 'Roman',
    'rok': 2017,
    'dochazka': 0.95,
    'vyznamenani': True
}
print(absolvent['jmeno'])
print(absolvent['vyznamenani'])

#seznam absolventů našeho kurzu:
absolventi = [
    {'jmeno': 'Petr', 'prijmeni': 'Roman', 'rok': 2017, 'dochazka': 0.95, 'vyznamenani': True},
    {'jmeno': 'Jana', 'prijmeni': 'Kočanská', 'rok': 2015, 'dochazka': 0.92, 'vyznamenani': True},
    {'jmeno': 'Eva', 'prijmeni': 'Horká', 'rok': 2014, 'dochazka': 0.85, 'vyznamenani': False},
    {'jmeno': 'Ivo', 'prijmeni': 'Roubeník', 'rok': 2017, 'dochazka': 0.75, 'vyznamenani': False}
]

#příjmení absolventa na indexu 2
print (absolventi[2]['prijmeni'])

#spočítat jejich průměrnou docházku na kurz.
from statistics import mean
#pouziji chroustani seznamu
seznam_dochazek = [absolvent['dochazka'] for absolvent in absolventi]
print(mean(seznam_dochazek))

dochazka = mean([ab['dochazka'] for ab in absolventi])
print(dochazka)

#SLOZITJSI STRUKTURY
kurz = {
    'nazev': 'Úvod do programování',
    'lektor': 'Martin Podloucký',
    # je to seznam konani
    'konani': [
        {
            'misto': 'T-Mobile',
            'koucove': [
                'Dan Vrátil',
                'Filip Kopecký',
                'Martina Nemčoková'
            ],
            'ucastnic': 30
        },
        {
            'misto': 'MSD IT',
            'koucove': [
                'Dan Vrátil',
                'Zuzana Tučková',
                'Martina Nemčoková'
            ],
            'ucastnic': 25
        },
        {
            'misto': 'Škoda DigiLab',
            'koucove': [
                'Dan Vrátil',
                'Filip Kopecký',
                'Kateřina Kalášková'
            ],
            'ucastnic': 41
        }
    ]
}
print (kurz['konani'][1]['koucove'])

#chci vypsat pocty ucastnic
#zpusob 1
pocty_ucastnic = [konani['ucastnic'] for konani in kurz['konani']]
print(pocty_ucastnic)

#zpusob 2
for kon in kurz['konani']:
    print(kon['ucastnic'])

kouc  = kurz['konani'][1]['koucove']
print(kouc)
