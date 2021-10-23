from Grafo import Grafo
from VetorOrdenado import VetorOrdenado
from Greedy import Greedy

grafo = Grafo()
vetor = VetorOrdenado(5)
gulosa = Greedy(grafo.bucharest)

grafo.arad.mostra_adjacentes()
grafo.bucharest.mostra_adjacentes()

vetor.insere(grafo.arad)
vetor.insere(grafo.craiova)
vetor.insere(grafo.bucharest)
vetor.insere(grafo.dobreta)

gulosa.buscar(grafo.arad)
