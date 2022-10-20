import statistics

with open('hody2.txt') as vstup:
    hody = vstup.readlines()
hody = [int(hod) for hod in hody]

if len(hody) < 1000:
    print('Nespolehlivý výsledek kvůli nedostatku dat.')
else:
    print('vysledek je spravny')

print(statistics.mean(hody))