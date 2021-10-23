from Grafo import Grafo
from VetorOrdenado import VetorOrdenado
from AEstrela import AEstrela

grafo = Grafo()

vetor = VetorOrdenado(3)
vetor.insereEstrela(grafo.arad.adjacentes[0])
vetor.insereEstrela(grafo.arad.adjacentes[1])
vetor.insereEstrela(grafo.arad.adjacentes[2])

busca_estrela = AEstrela(grafo.bucharest)
busca_estrela.buscar(grafo.arad)
