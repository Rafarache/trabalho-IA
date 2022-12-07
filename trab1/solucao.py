"""
CONSTANTES
"""

ESQUERDA = "esquerda"
DIREITA = "direita"
CIMA = "cima"
BAIXO = "baixo"

OBJECTIVE = "12345678_"


def estadoparaarray(estado):
    array = [[] for i in range(3)]
    for x in range(3):
        for y in range(3):
            array[y].append(estado[x + (y*3)])

    return array
    
def arrayparaestado(array):
    string = ""
    for x in range(3):
        for y in range(3):
            string += array[x][y]
    
    return string

def posicaoespaco(array):
    ax = 0
    ay = 0
    for y in range(3):
        for x in range(3):
            if (array[x][y] == "_"):
                ax = x
                ay = y
    
    return (ax, ay)


class Nodo:
    def __init__(self, estado, pai, acao, custo):
        self.estado = estado #string
        self.pai = pai #Nodo
        self.acao = acao #string
        self.custo = custo #int
                
    def mostrar(self):
        if(self.pai != None):
            return self.estado + " " + self.acao + " Pai -> " + self.pai.estado + str(self.custo)
        else:
            return self.estado
        
    def __str__(self):
        return self.mostrar()

    def __repr__(self):
        return self.mostrar()


def sucessor(estado):
    """
    Recebe um estado (string) e retorna uma lista de tuplas (ação,estado atingido)
    para cada ação possível no estado recebido.
    Tanto a ação quanto o estado atingido são strings também.
    :param estado:
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    arrayestado = estadoparaarray(estado)
    listadeestadospossiveis = []
    x,y = posicaoespaco(arrayestado)
    if (y<2):
        newestado = estadoparaarray(estado)
        newestado[x][y] = newestado[x][y+1]
        newestado[x][y+1] = "_"
        listadeestadospossiveis.append((DIREITA, arrayparaestado(newestado)))
    
    if (x<2):
        newestado = estadoparaarray(estado)
        newestado[x][y] = newestado[x+1][y]
        newestado[x+1][y] = "_"
        listadeestadospossiveis.append((BAIXO, arrayparaestado(newestado)))

    if (y>0):
        newestado = estadoparaarray(estado)
        newestado[x][y] = newestado[x][y-1]
        newestado[x][y-1] = "_"
        listadeestadospossiveis.append((ESQUERDA, arrayparaestado(newestado)))

    if (x>0):
        newestado = estadoparaarray(estado)
        newestado[x][y] = newestado[x-1][y]
        newestado[x-1][y] = "_"
        listadeestadospossiveis.append((CIMA, arrayparaestado(newestado)))
        
    return listadeestadospossiveis

def expande(nodo):
    """
    Recebe um nodo (objeto da classe Nodo) e retorna um iterable de nodos.
    Cada nodo do iterable é contém um estado sucessor do nó recebido.
    :param nodo: objeto da classe Nodo
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    sucessores = sucessor(nodo.estado)
    lista = []
    for acao, estado in sucessores:
        lista.append(Nodo(estado, nodo, acao, 1))
    
    return lista
	
def pegarcaminhoaraiz(nodo):
    arraydirecao = []
    nodoaux = nodo
    pai = nodoaux.pai
    while pai != None:
        arraydirecao.append(nodo.acao)
        nodoaux = nodoaux.pai
        pai = nodoaux.pai
        
    return list(reversed(arraydirecao))

def bfs(estado):
    """
    Recebe um estado (string), executa a busca em LARGURA e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    inicial = Nodo(estado, None, None, 1)
    exploradas = []
    fronteiras = [inicial]
    atual = None
    while True:
        #print(exploradas, fronteiras, atual)
        if(len(fronteiras) == 0):
            return None
        atual = fronteiras.pop(0)
        if(atual.estado == OBJECTIVE):
            return pegarcaminhoaraiz(atual)
        if not any(atual.estado in explorada.estado for explorada in exploradas):
            exploradas.append(atual)
            fronteiras += expande(atual)

def dfs(estado):
    """
    Recebe um estado (string), executa a busca em PROFUNDIDADE e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo


def astar_hamming(estado):
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Hamming e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo


def astar_manhattan(estado):
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Manhattan e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    
    
# print(arrayparaestado(estadoparaarray(OBJECTIVE)))
# print(sucessor(OBJECTIVE))
# print(expande(Nodo(OBJECTIVE, None, None, 1)))
print(bfs("123_56478"))
