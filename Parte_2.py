# --- Situacion de la vida real ---

# Sistema de categorías y productos en una tienda de comercio electrónico (Tecnology Store):
# La estructura representa el menú de navegación de un sitio web de ventas departamentales, 
# donde se organizan los departamentos principales, las subcategorías y finalmente los artículos 
# individuales disponibles para la compra.

# Nodos: Sistema de categorías y productos (Tecnology Store)
import networkx as nx
import matplotlib.pyplot as plt

V = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
A = {(1,2), (1,3), 
     (2,4), (2,5), 
     (3,6), (3,7), 
     (4,8),
     (5,9), (5,10), 
     (6,11), 
     (7,12)
     }

print("Vértices (Elementos del catálogo):", V)
print("Aristas (Relaciones jerárquicas de pertenencia):", A)  

Nodo_raiz = 1                 # Catálogo general de la tienda en línea
nodos_internos = {2,3,4,5,6,7}  # Departamentos y subcategorías (Tecnología, Computación, Telefonía)
Nodo_hoja = {8,9,10,11,12}    # Productos finales listos para la venta (Laptops, Smartphones)

print("Nodo raíz (Catálogo):", Nodo_raiz)
print("Nodos internos (Departamentos/Subcategorías):", nodos_internos) 
print("Nodos hoja (Productos):", Nodo_hoja)

# ------------------------------------------------

# Recorridos del árbol: Menú de navegación departamental
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

print("\nEstructura jerárquica del Árbol:")
for nodo, hijos in arbol.items():
    print(f"Nodo {nodo}: {hijos}")