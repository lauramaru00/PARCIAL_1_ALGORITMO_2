# --- Situacion de la vida real ---

# Sistema de categorías y productos en una tienda de comercio electrónico (Tecnology Store):
# La estructura representa el menú de navegación de un sitio web de ventas departamentales, 
# donde se organizan los departamentos principales, las subcategorías y finalmente los artículos 
# individuales disponibles para la compra.

# Nodos: Sistema de categorías y productos (Tecnology Store)
import networkx as nx
import matplotlib.pyplot as plt

empresa = {
    1: "Catálogo Tecnológico",
    2: "Computación",
    3: "Telefonía",
    4: "Laptops",
    5: "Componentes",
    6: "Smartphones",
    7: "Accesorios Móviles",
    8: "Laptop Gamer 16\"",
    9: "Tarjeta Gráfica RTX",
    10: "Memoria RAM 32GB",
    11: "Smartphone 256GB",
    12: "Cargador Rápido 65W",
}

V = {empresa[i] for i in range(1, 13)}

aristas_id = [
    (1, 2), (1, 3),
    (2, 4), (2, 5),
    (3, 6), (3, 7),
    (4, 8),
    (5, 9), (5, 10),
    (6, 11),
    (7, 12),
]

A = {(empresa[u], empresa[v]) for u, v in aristas_id}

print("Vértices (Elementos del catálogo):", V)
print("Aristas (Relaciones jerárquicas de pertenencia):", A)

Nodo_raiz = empresa[1]                          # Catálogo general de la tienda en línea
nodos_internos = {empresa[i] for i in range(2, 8)}  # Departamentos y subcategorías
Nodo_hoja = {empresa[i] for i in range(8, 13)}     # Productos finales listos para la venta

print("\nNodo raíz (Catálogo):", Nodo_raiz)
print("Nodos internos (Departamentos/Subcategorías):", nodos_internos)
print("Nodos hoja (Productos):", Nodo_hoja)

# ------------------------------------------------
# Recorridos / estructura del árbol: Menú de navegación departamental
arbol_id = {
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
    12: [],
}

arbol = {
    empresa[nodo]: [empresa[hijo] for hijo in hijos]
    for nodo, hijos in arbol_id.items()
}

print("\nEstructura jerárquica del Árbol:")
for nodo, hijos in arbol.items():
    print(f"  {nodo} -> {hijos}")

# ------------------------------------------------
# Visualización gráfica del árbol con empresa en cada nodo
G = nx.DiGraph()
G.add_nodes_from(V)
G.add_edges_from(A)

# posiciones para los nodos del árbol (ajustadas para una mejor visualización)
pos = {
    "Catálogo Tecnológico": (0, 3),
    "Computación": (-3, 2),
    "Telefonía": (3, 2),
    "Laptops": (-4.5, 1),
    "Componentes": (-1.5, 1),
    "Smartphones": (1.5, 1),
    "Accesorios Móviles": (4.5, 1),
    "Laptop Gamer 16\"": (-4.5, 0),
    "Tarjeta Gráfica RTX": (-2.4, 0),
    "Memoria RAM 32GB": (-0.6, 0),
    "Smartphone 256GB": (1.5, 0),
    "Cargador Rápido 65W": (4.5, 0),
}

colores = []
for nodo in G.nodes():
    if nodo == Nodo_raiz:
        colores.append("#4A90E2")       # Raíz
    elif nodo in nodos_internos:
        colores.append("#7ED321")       # Departamentos / subcategorías
    else:
        colores.append("#F5A623")       # Productos finales (hojas)

plt.figure(figsize=(14, 7))
nx.draw(
    G,
    pos=pos,
    with_labels=True,
    node_color=colores,
    node_size=8800,
    font_size=8.5,
    font_weight="bold",
    arrows=True,
    arrowsize=15,
    edge_color="#666666",
)
plt.title("Menú Jerárquico — Technology Store", fontsize=13, fontweight="bold")
plt.axis("off")
plt.tight_layout()
plt.show()