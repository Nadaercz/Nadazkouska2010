jmena = ['Roman', 'Jana', 'Radek', 'Petra', 'Vlasta']

# pridali odradkovani
jmena_s_entrem = [jmeno + '\n' for jmeno in jmena]

# zapsali
with open('uzivatele.txt', mode='w', encoding='utf-8') as vystup:
    vystup.writelines(jmena_s_entrem)

# a hned nacetli
with open('uzivatele.txt', mode='r', encoding='utf-8') as vstup:
    nactene_radky = vstup.readlines()

print(nactene_radky)