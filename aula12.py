def somar(function):
    def interna(*args, **kwars):
        resultado = function(*args, **kwars)
        return resultado
    return interna




def soma(x, y):
    return x + y



valor = somar(soma)

print(valor(2, 2))