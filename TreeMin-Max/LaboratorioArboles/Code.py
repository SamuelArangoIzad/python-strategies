class Grafo:
    def __init__(self):
        self.vertices = set()
        self.aristas = []

    def agregar_arista(self, inicio, fin, peso):
        self.aristas.append((inicio, fin, peso))
        self.vertices.add(inicio)
        self.vertices.add(fin)

def buscar(ancestros, vertice):
    if ancestros[vertice] != vertice:
        ancestros[vertice] = buscar(ancestros, ancestros[vertice])
    return ancestros[vertice]

def unir(ancestros, rango, x, y):
    raiz_x = buscar(ancestros, x)
    raiz_y = buscar(ancestros, y)

    if raiz_x != raiz_y:
        if rango[raiz_x] < rango[raiz_y]:
            raiz_x, raiz_y = raiz_y, raiz_x
        ancestros[raiz_y] = raiz_x
        if rango[raiz_x] == rango[raiz_y]:
            rango[raiz_x] += 1

def kruskal(grafo, tipo):
    aristas_ordenadas = sorted(grafo.aristas, key=lambda x: x[2], reverse=(tipo == "max"))

    ancestros = {vertice: vertice for vertice in grafo.vertices}
    rango = {vertice: 0 for vertice in grafo.vertices}

    arbol = Grafo()

    for arista in aristas_ordenadas:
        inicio, fin, peso = arista
        if buscar(ancestros, inicio) != buscar(ancestros, fin):
            arbol.agregar_arista(inicio, fin, peso)
            unir(ancestros, rango, inicio, fin)

    return arbol

# Crear el grafo
grafo = Grafo()
grafo.agregar_arista('A', 'B', 10)
grafo.agregar_arista('A', 'C', 8)
grafo.agregar_arista('A', 'D', 15)
grafo.agregar_arista('B', 'E', 15)
grafo.agregar_arista('C', 'J', 14)
grafo.agregar_arista('C', 'G', 15)
grafo.agregar_arista('D', 'I', 15)
grafo.agregar_arista('D', 'G', 6)
grafo.agregar_arista('E', 'H', 30)
grafo.agregar_arista('E', 'J', 8)
grafo.agregar_arista('G', 'I', 7)
grafo.agregar_arista('G', 'F', 8)
grafo.agregar_arista('J', 'F', 9)
grafo.agregar_arista('J', 'H', 18)
grafo.agregar_arista('F', 'L', 15)
grafo.agregar_arista('I', 'K', 10)
grafo.agregar_arista('K', 'L', 10)
grafo.agregar_arista('H', 'L', 15)

# Obtener árbol mínimo
arbol_minimo = kruskal(grafo, "min")
print("Árbol mínimo:")
for arista in arbol_minimo.aristas:
    print(arista)

# Obtener árbol máximo
arbol_maximo = kruskal(grafo, "max")
print("\nÁrbol máximo:")
for arista in arbol_maximo.aristas:
    print(arista)