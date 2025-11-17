# Template genérico — SKELETON
# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}
# Algoritmo Gnome Sort

items = []
n = 0
# Agregá acá tus punteros/estado, p.ej.:
# i = 0; j = 0; fase = "x"; stack = []

#Estado del Gnome Sort
pos=0

def init(vals):
    global items,n,pos
    items = list(vals)
    n = len(items)

def step():
    global items,n,pos

    #Si ya terminó.
    if n<=1 or pos>=n:  
        return {"done":True}
    
    #Si estamos al principio, solo avanzamos.
    if pos==0:  
        pos+=1
        return{"a":0,"b":0,"swap":False,"done":False}
    
    a=pos-1
    b=pos

    #Caso 1: desorden -> swap y retrocedemos.
    if items[a]>items[b]:
        items[a],items[b] = items[b],items[a]
        pos-=1
        return {"a":a,"b":b,"swap":True,"done":False}
    
    # Caso 2: orden -> avanzamos.
    else:
        pos+=1
        return {"a":a,"b":b,"swap":False,"done":False}

    """    
    # TODO: inicializar punteros/estado
    """

    # TODO: implementar UN micro-paso de tu algoritmo y devolver el dict.
    # Recordá:
    # - a, b dentro de [0, n-1]
    # - si swap=True, primero hacé el intercambio en 'items'
    # - cuando termines, devolvé {"done": True}
    # return {"done": True}