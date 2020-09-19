# se reciben 2 números y se retorna la suma, resta o multiplicación de ellos
def func(a, b, c):
    if c == 0:
        d = a+b
        return d
    if c == 1:
        d = a-b
        return d
    if c == 2:
        d = a*b
        return d
    return "eror"
