with open('mereni.txt', encoding='utf-8') as vstup:
    radky = vstup.readlines()

radky = [radek.split('\t') for radek in radky]
radky = [[radek[0], float(radek[1])] for radek in radky]
print(radky)