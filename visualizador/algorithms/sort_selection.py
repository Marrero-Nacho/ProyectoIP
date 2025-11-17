# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i = 0          # cabeza de la parte no ordenada
j = 0          # cursor que recorre y busca el mínimo
min_idx = 0    # índice del mínimo de la pasada actual
fase = "buscar"  # "buscar" | "swap"

def init(vals):
    global items, n, i, j, min_idx, fase
    items = list(vals)
    n = len(items)
    i = 0
    j = i + 1
    min_idx = i
    fase = "buscar"

def step():
    # TODO:
    # - Fase "buscar": comparar j con min_idx, actualizar min_idx, avanzar j.
    #   Devolver {"a": min_idx, "b": j_actual, "swap": False, "done": False}.
    #   Al terminar el barrido, pasar a fase "swap".
    # - Fase "swap": si min_idx != i, hacer ese único swap y devolverlo.
    #   Luego avanzar i, reiniciar j=i+1 y min_idx=i, volver a "buscar".
    #
    # Cuando i llegue al final, devolvé {"done": True}.
    
    global items, n, i, j, min_idx, fase

    # 1) Si i llegó a n-1, ya no quedan pasadas
    if i >= n - 1:
        return {"done": True}

    # -------------------------
    # FASE 1: BUSCAR MÍNIMO
    # -------------------------
    if fase == "buscar":
        # Si j está dentro del rango, seguimos comparando
        if j < n:
            # Comparar el elemento actual con el mínimo encontrado
            actual_j = j
            if items[actual_j] < items[min_idx]:
                min_idx = actual_j

            # Avanzar j para la siguiente llamada
            j += 1

            return {
                "a": min_idx,
                "b": actual_j,
                "swap": False,
                "done": False
            }

        # Si j salió del rango → terminamos la fase de búsqueda
        fase = "swap"

    # -------------------------
    # FASE 2: HACER EL SWAP
    # -------------------------
    if fase == "swap":
        # Si el mínimo no está en i → hacemos el swap
        if min_idx != i:
            items[i], items[min_idx] = items[min_idx], items[i]

            # Después del swap se avanza i y se reinician valores,
            # pero devolvemos primero el swap visual
            old_i = i
            old_min = min_idx

            # Preparar para la siguiente pasada
            i += 1
            j = i + 1
            min_idx = i
            fase = "buscar"

            return {
                "a": old_i,
                "b": old_min,
                "swap": True,
                "done": False
            }

        # Si no hay swap, igual debemos avanzar i
        i += 1
        j = i + 1
        min_idx = i
        fase = "buscar"

        # Devolver highlight sin swap
        return {
            "a": i - 1,
            "b": min_idx,
            "swap": False,
            "done": False
        }
