import random
import sys

pocet_hodu = int(sys.argv[1])

hody_kostkou = [random.randint(1, 6) for _ in range(pocet_hodu)]
hody_kostkou_s_entry = [str(hod) + '\n' for hod in hody_kostkou]

with open('hody2.txt', mode='w', encoding='utf-8') as vystup:
    vystup.writelines(hody_kostkou_s_entry)