from queue import Queue,LifoQueue

"""
CONSTANTES
"""

ESQUERDA = "esquerda"
DIREITA = "direita"
CIMA = "acima"
BAIXO = "abaixo"

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
        self.custoAgregado  = None # int
                
    def mostrar(self):
        if(self.pai != None):
            return self.estado + " " + self.acao + " Pai -> " + self.pai.estado +  " " +  str(self.custoAgregado)
        else:
            return self.estado + " sem pai e mae"
        
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
        lista.append(Nodo(estado, nodo, acao, nodo.custo + 1))
    
    return lista
	
def pegarcaminhoaraiz(nodo):
    arraydirecao = []
    nodoaux = nodo
    pai = nodoaux.pai
    while pai != None:
        arraydirecao.append(nodoaux.acao)
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
    exploradas = {}
    fronteiras = Queue(0)
    fronteiras.put(inicial)
    atual = None
    while True:
        #print(exploradas, fronteiras, atual)
        if(fronteiras.qsize() == 0):
            return None
        atual = fronteiras.get()
        if(atual.estado == OBJECTIVE):
            return pegarcaminhoaraiz(atual)
        if not atual.estado in exploradas:
            exploradas[atual.estado] = atual
	    #fronteiras += expande(atual)
            for node in expande(atual):
                fronteiras.put(node)

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
    inicial = Nodo(estado, None, None, 1)
    exploradas = {}
    fronteiras = LifoQueue(0)
    fronteiras.put(inicial)
    atual = None
    while True:
        #print(exploradas, fronteiras, atual)
        if(fronteiras.qsize() == 0):
            return None
        atual = fronteiras.get()
        if(atual.estado == OBJECTIVE):
            return pegarcaminhoaraiz(atual)
        if not atual.estado in exploradas:
            exploradas[atual.estado] = atual
	    #fronteiras += expande(atual)
            for node in expande(atual):
                fronteiras.put(node)

def numerodepecasforadelugar(estado):
    soma = 0
    for x in range(9):
        if(estado[x] == OBJECTIVE[x]):
            soma += 1

    return 9 - soma

  
def pegarnododemenorcusto(dic):
    menor = 1000000
    for nodo in dic:
        if nodo < menor and len(dic[nodo]) != 0:
            menor = nodo

    ret = dic[menor].pop(0)
    return ret

def valormanhattan(estado):
    soma = 0
    for x, linha in enumerate(estadoparaarray(estado)):
        for y, valor in enumerate(linha):
            if(valor != "_"):
                #print(x,y, valor, estado)
                soma += abs((int(valor)-1)%3 - x%3)
                soma += abs((int(valor)-1)%3 - y%3)
    return soma
    
def pegarnododemenorcustomanhattan(array):
    menor = array[0]
    #print(array)
    for nodo in array:
        custonodo = nodo.custo + valormanhattan(nodo.estado)
        customenor = menor.custo + valormanhattan(menor.estado)
        #print(custonodo, customenor, nodo, menor)
        if (custonodo < customenor):
            menor = nodo
    return menor

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
    inicial = Nodo(estado, None, None, 1)
    exploradas = {}
    inicial.custoAgregado = numerodepecasforadelugar(inicial.estado) + inicial.custo
    fronteiras = {inicial.custoAgregado: [inicial]}
    atual = None
    while True:

        #print(len(exploradas))
        if(len(fronteiras) == 0):
            return None
        atual = pegarnododemenorcusto(fronteiras)
        if(atual.estado == OBJECTIVE):
            return pegarcaminhoaraiz(atual)
        #print(atual)
        if not atual.estado in exploradas:
            exploradas[atual.estado] = atual
            for node in expande(atual):
                node.custoAgregado = numerodepecasforadelugar(node.estado) + node.custo
                if not node.custoAgregado in fronteiras:
                    fronteiras[node.custoAgregado] = [node]
                else:
                    fronteiras[node.custoAgregado] = fronteiras[node.custoAgregado] + [node]
        
        #print("***", exploradas)
        #print("-->", atual) 

	


def astar_manhattan(estado):
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Manhattan e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    inicial = Nodo(estado, None, None, 1)
    exploradas = {}
    inicial.custoAgregado = valormanhattan(inicial.estado) + inicial.custo
    fronteiras = {inicial.custoAgregado: [inicial]}
    atual = None
    while True:

        #print(len(fronteiras))
        if(len(fronteiras) == 0):
            return None
        atual = pegarnododemenorcusto(fronteiras)
        if(atual.estado == OBJECTIVE):
            return pegarcaminhoaraiz(atual)
        #print(atual)
        if not atual.estado in exploradas:
            exploradas[atual.estado] = atual
            for node in expande(atual):
                node.custoAgregado = valormanhattan(node.estado) + node.custo
                if not node.custoAgregado in fronteiras:
                    fronteiras[node.custoAgregado] = [node]
                else:
                    fronteiras[node.custoAgregado] = fronteiras[node.custoAgregado] + [node]
        

START = "185423_67"
#print(dfs(START))
#print(dfs(START))
#print(astar_hamming(START))
#print(astar_manhattan(START))
