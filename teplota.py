mereni = [
  ['po', 17.3],
  ['út', 16.8],
  ['st', 15.1],
  ['čt', 13.2],
  ['pá', 14.0],
  ['so', 13.9],
  ['ne', 15.8]
]
teploty = [radek[1] for radek in mereni]
prumer = sum(teploty)/len(teploty)
#radkovy komentar """viceradkovy komentar"""
rozdily = [round(abs(t - prumer),2) for t in teploty]
#hledam nejmensi odchylku od prumeru
min_rozdil = min(rozdily)
index = rozdily.index(min_rozdil)
print(index)
print(mereni[index][0])
print(
  'Den s teplotou nejblíž průměru je ' + mereni[index][0])

