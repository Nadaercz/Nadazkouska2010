import sys

prvniCislo = int(sys.argv[1])
druheCislo = int(sys.argv[2])

if druheCislo == 0:
    print('Nulou se delit nelze')
else:
    podilCisel=prvniCislo / druheCislo 
    print(f"Podil cisel {prvniCislo} a {druheCislo} je {round(podilCisel,3)}")