import sys
hodinova_mzda = int(sys.argv[1])
print(hodinova_mzda)

with open('vykaz.txt', encoding='utf-8') as vstup:
    hodiny_jako_text = vstup.readlines()
seznam_hodin = [int(hodina_text) for hodina_text in hodiny_jako_text]

print(seznam_hodin)

platy = [hodinova_mzda*hodiny for hodiny in seznam_hodin]
print(platy)

print ('vyplata za rok je ', sum(platy))