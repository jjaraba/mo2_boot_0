from functools import reduce

def doble(x):
    return x+x

def esPar(x):
    return x % 2 == 0
def SumatorioClasico(l):
    resultado = 0
    for valor in l:
        resultado += valor
        
    return resultado

def SumatorioDobleClasico(l):
    resultado = 0
    for valor in l:
        resultado += valor *2
        
    return resultado


def ProductoTotal(l):
    resultado = 1
    for valor in l:
        resultado *= valor
    return resultado

lista = [1, 3, -1, 15, 9]


listaDoble = map(lambda x: x*2, lista)
listaDoble1= map(doble, lista)

listaPares = filter(lambda x: x % 2 ==0, lista)
listaPares1 =filter(esPar, lista)

sumatorio = reduce(lambda x, y: x + y, lista)
#Creo una copia de la lista
l=lista[:]
# Añado el neutro para la sum en la posicion cero
l.insert(0,0)

suma100 = reduce(lambda x,y: x+y, range(101))
sumatorioDobles = reduce(lambda x,y: x + y * 2, l)


print (list(listaPares))
print (list(listaPares1))

print (sumatorio)
print ("sumatorio doble",sumatorioDobles)

print (suma100)


