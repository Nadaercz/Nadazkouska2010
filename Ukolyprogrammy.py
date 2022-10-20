#Napište program, který na obrazovku vypíše vaše jméno a na nový řádek město, ze kterého pocházíte
a = "Nada"
b = "Kirov"
print ('Vase jmeno je '+ a)
print ('Město, ze kterého pocházíte, je ' + b)
#Na první lekci jsme dělali cvičení na výpočet výplaty pomocí proměnných. 
#Udělejte toto cvičení znova, ale tentokrát jako program. Nejdříve uložte nezbytné hodnoty do proměnných, 
#spočítejte výplatu a pak ji pomocí funkce print() vypište na obrazovku.
c = 7
d = 450
e = 21
f = c * d * e
print('Vas měsíční příjem je ' + str(f))
print("Vas mesicni prijem je ", f)
# ukol 3 - Teploty jako program
teploty = [
  [2.1, 5.2, 6.1, -0.1],
  [2.2, 4.8, 5.6, -1.0],
  [3.3, 6.5, 5.9, 1.2],
  [2.9, 5.6, 6.0, 0.0],
  [2.0, 4.6, 5.5, -1.2],
  [1.0, 3.2, 2.1, -2.0],
  [0.4, 2.7, 1.3, -2.8]
]
q = [sum(x)/len(x) for x in teploty] 
w = [x[0] for x in teploty]
e = [x[-1] for x in teploty]
r = [[x[1],x[-1]] for x in teploty]
t = sum(sum(x)/len(x) for x in teploty)/7
print(q)
print(w)
print(e)
print(e)
print(r)
print(t)