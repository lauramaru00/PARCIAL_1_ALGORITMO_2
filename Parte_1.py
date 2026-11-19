# Nodos.
import networkx as nx
import matplotlib.pyplot as plt

V = {1,2,3,4,5,6,7,8,9,10,11,12};
A = {(1,2), (1,3), 
     (2,4), (2,5), 
     (3,6), (3,7), 
     (4,8),
     (5,9), (5,10), 
     (6,11), 
     (7,12)
     };

print("Vertices:", V)
print("Aristas:", A)  

Nodo_raiz = 1
Nodo_hoja = {8,9,10,11,12}
nodos_internos = {2,3,4,5,6,7}

print("Nodo raiz:", Nodo_raiz)
print("Nodos hoja:", Nodo_hoja) 
print("Nodos internos:", nodos_internos)

# ------------------------------------------------

# Recorridos del arbol.

arbol = {
    1: [2, 3],
    2: [4, 5],
    3: [6, 7],
    4: [8],
    5: [9, 10],
    6: [11],
    7: [12],
    8: [],
    9: [],
    10: [],
    11: [],
    12: []
}
print("Árbol:")
for nodo, hijos in arbol.items():
    print(f"{nodo}: {hijos}")


#Recorridos del arbol


preorden = [1,2,4,8,5,9,10,3,6,11,7,12]
inorden = [8,4,2,9,5,10,1,6,11,3,12,7]
postorden = [8,4,9,10,5,2,11,6,12,7,3,1]

print("Recorrido en preorden:", preorden)
print("Recorrido en inorden:", inorden)
print("Recorrido en postorden:", postorden)