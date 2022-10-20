kurz = {
    'nazev': 'Úvod do programování',
    'lektor': 'Martin Podloucký',
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
#počet účastnic na posledním konání kurzu.
print(kurz['konani'][-1]['ucastnic'])

#jméno posledního kouče na prvním konání kurzu
print(kurz['konani'][1]['koucove'][-1])

#celkový počet konání kurzu.
print(len(kurz['konani']))

#všechna místa, na kterých se kurz konal.
#vystup jako seznam 
seznam_mist = [konani['misto'] for konani in kurz['konani']]
print(seznam_mist)

#variant 2
#vystup do sloupce
for konani in kurz['konani']:
    print(konani['misto'])