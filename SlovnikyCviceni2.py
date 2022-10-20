kniha = {
    'nazev' : 'Babicka',
    'autori' :[
        {
        'krestni':'Bozena',
        'prijmeni':'Nemcova',
        'zije':False,
        },
        {
        'krestni':'Jara',
        'prijmeni':'Cimrman',
        'zije':True,
        },
    ],
    'pocet_vytisku':100,
    }
print(kniha['autori'])

for autor in kniha['autori']:
    cele_jmeno= autor['krestni']+' '+autor['prijmeni']
    print(cele_jmeno)
