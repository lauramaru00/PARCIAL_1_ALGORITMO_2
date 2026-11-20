import matplotlib.pyplot as plt
import networkx as nx

# 1. Definición formal del árbol (Vértices y Aristas)
V = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
A = [
    (1, 2),
    (1, 3),
    (2, 4),
    (2, 5),
    (3, 6),
    (3, 7),
    (4, 8),
    (5, 9),
    (5, 10),
    (6, 11),
    (7, 12),
]

nodo_raiz = 1
nodo_hoja = {8, 9, 10, 11, 12}
nodos_internos = {2, 3, 4, 5, 6, 7}

# Generar diccionario de adyacencia automáticamente para los recorridos
arbol = {v: [hijo for padre, hijo in A if padre == v] for v in V}

# 2. Creación del grafo dirigido (código corto con NetworkX)
G = nx.DiGraph()
G.add_edges_from(A)


# 3. Definición de funciones de recorrido del árbol
def preorden(nodo, tree, resultado=None):
  if resultado is None:
    resultado = []
  resultado.append(nodo)
  for hijo in tree.get(nodo, []):
    preorden(hijo, tree, resultado)
  return resultado


def inorden(nodo, tree, resultado=None):
  if resultado is None:
    resultado = []
  hijos = tree.get(nodo, [])
  if len(hijos) > 0:
    inorden(hijos[0], tree, resultado)  # Hijo izquierdo
  resultado.append(nodo)  # Raíz
  for hijo in hijos[1:]:
    inorden(hijo, tree, resultado)  # Hijo derecho (si existe)
  return resultado


def postorden(nodo, tree, resultado=None):
  if resultado is None:
    resultado = []
  for hijo in tree.get(nodo, []):
    postorden(hijo, tree, resultado)
  resultado.append(nodo)
  return resultado


# imprimir propiedades del árbol y recorridos
print("--- PROPIEDADES DEL ÁRBOL ---")
print("Vértices:", V)
print("Aristas:", A)
print("Nodo raíz:", nodo_raiz)
print("Nodos hoja:", nodo_hoja)
print("Nodos internos:", nodos_internos)

print("\n--- RECORRIDOS ---")
print("Preorden:  ", preorden(nodo_raiz, arbol))
print("Inorden:   ", inorden(nodo_raiz, arbol))
print("Postorden: ", postorden(nodo_raiz, arbol))

# 4. Visualización gráfica con NetworkX y Matplotlib
plt.figure(figsize=(9, 6))

# definir posiciones de los nodos para una mejor visualización
pos = {
    1: (0, 4),
    2: (-2, 2.5),
    3: (2, 2.5),
    4: (-3, 1),
    5: (-1, 1),
    6: (1, 1),
    7: (3, 1),
    8: (-3, -0.5),
    9: (-1.5, -0.5),
    10: (-0.5, -0.5),
    11: (1, -0.5),
    12: (3, -0.5),
}

# Dibujar el grafo
nx.draw(
    G,
    pos,
    with_labels=True,
    node_color="#2b8cbe",
    node_size=800,
    edge_color="#bdbdbd",
    linewidths=1.5,
    font_color="white",
    font_size=12,
    font_weight="bold",
    arrows=True,
    arrowsize=20,
)

plt.title(
    "Visualización del Árbol - Estructura de Datos",
    fontsize=14,
    fontweight="bold",
)
plt.axis("off")
plt.show()