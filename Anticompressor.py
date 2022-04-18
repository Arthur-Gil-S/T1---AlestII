##
# @author - Arthur Gil dos Santos
# PUCRS - Escola Politécnica
##

import time

### Dicitonary Structure ###

lines = []

with open('caso05.txt','r') as file:
    lines = file.readlines()

dicionario = {pair[0]: pair[2:].replace('\n','') for pair in lines}
key = dicionario.keys()
value = dicionario.values()

#################################


list_total = {}

def anticompressor(chr):
    if not list_total.__contains__(chr):
        cont = 0
        element = dicionario.get(chr) 
        if len(element) <= 0: 
            return 1
        else:
            for c in element:
                cont += anticompressor(c)
        list_total.update({chr:cont})
        return cont
    return list_total.get(chr)
    

def main():
   
    biggest_value = {}
    for key in dicionario.keys():
        x = anticompressor(key)
        biggest_value.update({key: x})

    big = max(biggest_value, key = biggest_value.get)
    
    print('Caso: ', file.name)
    print('Letra inicial: ', big)
    print('Tamanho: ', biggest_value.get(big))

    
inicio = time.time()
main()
fim = time.time()
total_time = fim - inicio
print('Tempo: ', total_time)

