# ERRORES
# 1) En caso de que los operandos no sean números enteros
# 2) En caso de que los operandos no sean del rango permitido
# 2) En caso de que la operación indicada no exista
# 3) En caso de que los Array de entrada no sean del mismo tamaño

# METODO 1
def Basic_Ops(a, b, op):
    # Lista de operaciones que tendrá la función.
    ops = ["suma", "resta", "AND", "OR"]
    # Si estas variables mantienen la condición False, significa que hay un
    # error en los parámetros indicados de la función.
    enteros = False
    rangoA = rangoB = False
    if (type(a) == int) and (type(b) == int):
        enteros = True
        if (a >= -127) and (a <= 127):
            rangoA = True
        if (b >= -127) and (b <= 127):
            rangoB = True
    # Si todas estas variables son verderas, entonces se prosigue a realizar
    # la operación seleccionada.
    x = enteros and rangoA and rangoB
    if x is True:
        # Se verifica que la operación seleccionada esté dentro de la lista
        # de operaciones definida anteriormente.
        if op in ops:
            if op == "suma":
                y = a + b
            if op == "resta":
                y = a - b
            if op == "AND":
                y = a & b
            if op == "OR":
                y = a | b
            return y
        else:
            return "ERROR # 3"
    else:
        if enteros is False:
            return "ERROR # 1"
        else:
            return "ERROR # 2"
# METODO 2


def Array_Ops(A1, A2, op):
    # a y b hacen referencia al tammaño de los Array de entrada.
    a = len(A1)
    b = len(A2)
    # variable para guardar el resultado final.
    result = []
    # Se verifica que ambos arreglos sean del mismo tamaño.
    if a == b:
        # Se recorre cada elemento de los arreglos, con el fin de realizar.
        # la operacion con cada uno.
        for i in range(0, a):
            y = Basic_Ops(A1[i], A2[i], op)
            # se verifica que se retorne un número entero.
            if (type(y) == int):
                result.append(Basic_Ops(A1[i], A2[i], op))
            # se retorna el resultado no entero del llamado a la func.
            else:
                return y
            i = i + 1
        return result
    else:
        return "ERROR # 4"
