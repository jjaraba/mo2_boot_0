def normal(i):
    return i

def cuadrado(x):
    return x * x


def sumatodos(limitTo, f):
    resutado =0
    for i in range(limitTo+1):
        resutado += f(i)
    
    return resutado

print (sumatodos (100, normal))
print (sumatodos (3,cuadrado))