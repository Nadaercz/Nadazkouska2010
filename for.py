jmena = ['petr', 'pavel', 'jitka', 'jana']
delky = [len(jmeno) for jmeno in jmena]
print(delky)

jmena = ['petr', 'pavel', 'jitka', 'jana']
for jmeno in jmena:
    print(len(jmeno))

jmena = ['petr', 'pavel', 'jitka', 'jana']
for jmeno in jmena:
    mail = jmeno + '@gmail.com'
    print(mail)

jmena = ['petr', 'pavel', 'jitka', '', 'jana']
for jmeno in jmena:
    if len(jmeno) < 1:
        mail = 'neplatný email'
    else:
        mail = jmeno + '@gmail.cz'
    print(mail)

jmena = ['petr', 'pavel', 'jitka', 'jana']
for jmeno in jmena:
    mail = jmeno + '@gmail.com'
    print(mail)

emaily = [jmeno + '@gmail.com' for jmeno in jmena]
print(emaily)

seznam = []
seznam.append('ahoj')
seznam.append('czechitas')
print(seznam)

cisla = [1,2,3,4,5,6,7,8]
soucet = 0
for cislo in cisla:
    soucet = soucet + cislo
