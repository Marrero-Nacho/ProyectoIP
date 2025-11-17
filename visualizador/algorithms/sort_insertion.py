# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i = 0      # elemento que queremos insertar
j = None   # cursor de desplazamiento hacia la izquierda (None = empezar)

def init(vals):
    global items, n, i, j
    items = list(vals)
    n = len(items)
    i = 1      # común: arrancar en el segundo elemento
    j = None

def step():
    # TODO:
    # - Si i >= n: devolver {"done": True}.
    # - Si j es None: empezar desplazamiento para el items[i] (p.ej., j = i) y devolver un highlight sin swap.
    # - Mientras j > 0 y items[j-1] > items[j]: hacer UN swap adyacente (j-1, j) y devolverlo con swap=True.
    # - Si ya no hay que desplazar: avanzar i y setear j=None.
    global items, n, i, j

    # 1) Si ya terminamos
    if i >= n:
        return {"done": True}

    # 2) Si j es None → empezar a desplazar
    if j is None:
        j = i
        return {
            "a": j - 1 if j > 0 else 0,
            "b": j,
            "swap": False,
            "done": False
        }

    # 3) Si todavía hay desplazamiento (comparar y swapear)
    if j > 0 and items[j - 1] > items[j]:
        # hacer UN swap
        items[j - 1], items[j] = items[j], items[j - 1]
        j -= 1

        return {
            "a": j,
            "b": j + 1,
            "swap": True,
            "done": False
        }

    # 4) Si no hay más desplazamiento → avanzar al siguiente i
    i += 1
    j = None
    return {
        "a": i - 1,
        "b": i,
        "swap": False,
        "done": False
    }