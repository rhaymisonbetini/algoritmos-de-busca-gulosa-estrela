from VetorOrdenado import VetorOrdenado

class Greedy:
    def __init__(self, objetivo):
        self.objetivo = objetivo
        self.encontrado = False

    def buscar(self, atual):
        print('-----')
        print('Atual: {}'.format(atual.rotulo))

        if atual == self.objetivo:
            self.encontrado = True
        else:
            vetor_ordenado = VetorOrdenado(len(atual.adjacentes))
            for adjacentes in atual.adjacentes:
                if adjacentes.vertice.visitado == False:
                    adjacentes.vertice.visitado = True
                    vetor_ordenado.insere(adjacentes.vertice)
            vetor_ordenado.imprime()

            if vetor_ordenado.valores[0] != None:
                self.buscar(vetor_ordenado.valores[0])
