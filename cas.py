import sys
celkem = int(sys.argv[1])
hodin = celkem // 60
minut = celkem % 60
print(str(hodin) + ':' + str(minut))