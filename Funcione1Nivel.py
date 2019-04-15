def normal(i):
    return i

def cuadrado(x):
    return x * x

def cubo(x):
    return x**3


def sumatodos(limitTo, f):
    resultado = 0
    for i in range(limitTo+1):
        resultado += f(i)
    
    return resultado

if __name__ == '__main__':
    print (sumatodos (100, normal))
    print (sumatodos (3,cuadrado))
