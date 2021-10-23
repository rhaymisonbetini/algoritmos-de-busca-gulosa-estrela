class Vertice:
    def __init__(self, rotulo, distancia_objetivo):
        self.rotulo = rotulo
        self.distancia_objetivo = distancia_objetivo
        self.visitado = False
        self.adjacentes = []

    def adiciona_adjacente(self, adjacentes):
        self.adjacentes.append(adjacentes)

    def mostra_adjacentes(self):
        for i in self.adjacentes:
            print(i.vertice.rotulo, i.custo)
