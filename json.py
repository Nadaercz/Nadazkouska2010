#import json
#with open('absolventi.json', encoding='utf-8') as soubor:
#    text = soubor.read()
#absolventi = json.loads(text)
#print(absolventi)

import json
with open('absolventi.json', encoding='utf-8') as soubor:
    absolventi = json.load(soubor)
print(absolventi)

