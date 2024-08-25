#class Signs:
#    __init__ (self):
#    self.f = open('sinalizacao.csv')
    
f = open('sinalizacao.csv')

#for line in f:
#    print(line)

#for line in f:
#    print(line.split())

#for line in f:
#    print(line.split(';'))

antiga = ''
primeira = True
ausente = []

for line in f:
    if primeira:
        primeira = False
        continue
    lista = line.strip().split(';')
    if antiga == '' or antiga > lista[4]:
        antiga = lista[4]
    if lista[13].strip() == '' or lista[14].strip() == '':
        ausente.append(lista)
    else:
        print(lista)

print(antiga)
print(ausente)
