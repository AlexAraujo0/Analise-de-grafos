# Importação das bibliotecas
import warnings
import random

warnings.filterwarnings(
    "ignore",
    message="pkg_resources is deprecated as an API.*",
    category=UserWarning
)

import networkx as nx
import gravis as gv


class Grafo:
    """Representa um grafo baseado na estrutura de dados do NetworkX.

    O grafo modela relações entre pessoas, turmas, áreas de interesse e o nó
    central "Ilum". Cada pessoa é associada a uma turma, a uma área de interesse
    e a um perfil.

    Atributos
    ---------
    G : networkx.Graph
        Grafo principal utilizado para armazenar nós, arestas e atributos.
    turmas : list[str]
        Lista de turmas cadastradas no grafo.
    interesses : list[str]
        Lista de interesses baseados nas cinco grandes áreas da Ilum:
        CD, LM, CM, CV e HU.
    perfis : list[str]
        Lista de perfis discentes. "Te" representa perfil teórico e "Exp"
        representa perfil experimental.
    codigo_cores : dict[str, str]
        Dicionário que associa cada turma a uma cor em formato hexadecimal.
    """

    def __init__(self):
        """Inicializa a estrutura do grafo e seus atributos básicos."""
        self.G = nx.Graph()

        self.turmas = ["T22", "T23", "T24", "T25", "T26"]
        self.interesses = ["CD", "LM", "CM", "CV", "HU"]
        self.perfis = ["Te", "Exp"]

        self.codigo_cores = {
            "T22": "#00538A",
            "T23": "#000000",
            "T24": "#007D34",
            "T25": "#FF6800",
            "T26": "#803E75"
        }

    def gerar_basicos(self):
        """Gera os nós básicos do grafo.
    
        Adiciona ao grafo os nós correspondentes às turmas, às áreas de interesse
        e ao nó central "Ilum".
        """
        
        for interesse in self.interesses:
            self.G.add_node(
                interesse,
                interesse=interesse
            )

        # Gerando as turmas
        for turma in self.turmas:
            self.G.add_node(
                turma,
                turma=turma,
                color=self.codigo_cores[turma]
            )

        self.G.add_node("Ilum")

    def gerar_nos(self, n, seed=None):
        """Gera nós de pessoas com atributos aleatórios.
        
        Cada pessoa é representada por um nó numérico. Os atributos de cada nó
        incluem turma, interesse, perfil e cor associada à turma.
    
        Parâmetros
        ----------
        n : int
            Número de pessoas a serem geradas.
        seed : int, opcional
            Semente utilizada para tornar a geração aleatória reprodutível.
        """

        if seed is not None:
            random.seed(seed)

        for i in range(1, n + 1):
            turma = random.choice(self.turmas)

            self.G.add_node(
                i,
                turma=turma,
                interesse=random.choice(self.interesses),
                perfil=random.choice(self.perfis),
                color=self.codigo_cores[turma],
            )

    def agrupar(self):
        """Cria arestas entre os nós de acordo com seus atributos.
    
        Conecta cada pessoa à sua respectiva turma e área de interesse. Também
        conecta os nós de turmas e interesses ao nó central "Ilum".
        """
        for no, attrs in self.G.nodes(data=True):

            # Agrupando pessoas às suas turmas e interesses
            if "perfil" in attrs:
                turma = attrs.get("turma")
                interesse = attrs.get("interesse")

                if turma in self.G.nodes:
                    self.G.add_edge(no, turma)

                if interesse in self.G.nodes:
                    self.G.add_edge(no, interesse)

            # Agrupando turmas e interesses à Ilum
            elif "turma" in attrs:
                self.G.add_edge(no, "Ilum")

            elif "interesse" in attrs:
                self.G.add_edge(no, "Ilum")

    def gerar(self, n, seed=None):
        """Gera o grafo completo.
    
        Reinicializa o grafo, cria os nós básicos, gera os nós de pessoas e adiciona
        as arestas entre pessoas, turmas, interesses e o nó central "Ilum".
    
        Parâmetros
        ----------
        n : int
            Número de pessoas a serem geradas.
        seed : int, opcional
            Semente utilizada para controlar a aleatoriedade da geração.
    
        Retorno
        -------
        networkx.Graph
            Grafo gerado com nós, arestas e atributos.
        """
        
        self.G = nx.Graph()
        self.gerar_basicos()
        self.gerar_nos(n, seed)
        self.agrupar()

        return self.G

    def preparar_renderizacao(self):
        """Prepara uma cópia do grafo para renderização.
    
        Atribui rótulos vazios aos nós de pessoas e mantém os rótulos dos demais
        nós, como turmas, interesses e o nó central "Ilum".
    
        Retorno
        -------
        networkx.Graph
            Cópia do grafo com o atributo ``label`` configurado para visualização.
        """
        
        render = self.G.copy()

        for no, attrs in render.nodes(data=True):
            if "perfil" in attrs:
                attrs["label"] = ""
            else:
                attrs["label"] = str(no)

        return render

    def visualizar(self, html=False):
        """Visualiza ou exporta o grafo.
    
        Prepara o grafo para renderização usando a biblioteca Gravis. Se html
        for verdadeiro, retorna o código HTML da visualização. Caso contrário,
        retorna o objeto de visualização gerado pelo Gravis.
    
        Parâmetros
        ----------
        html : bool, opcional
            Define se a visualização deve ser retornada como código HTML.
            O valor padrão é False.
    
        Retorno
        -------
        object or str
            Objeto de visualização do Gravis quando html=False ou código HTML
            da visualização quando html=True.
        """
        render = self.preparar_renderizacao()

        fig = gv.three(
            render,
            graph_height=490,
            edge_size_factor=0.1,
            node_label_data_source="label",
            show_details_toggle_button=False,
            show_menu_toggle_button=False,
        )

        if html:
            return fig.to_html()

        return fig

    def vizinhanca(self, no, dados=False):
        """Obtém a vizinhança de um nó.
    
        Retorna os vizinhos de um nó do grafo. Opcionalmente, também retorna os
        atributos associados a cada vizinho.
    
        Parâmetros
        ----------
        no : str or int
            Nó cuja vizinhança será analisada.
        dados : bool, opcional
            Define se os atributos dos vizinhos devem ser retornados.
            O valor padrão é False.
    
        Retorno
        -------
        list or dict
            Lista com os vizinhos quando dados=False ou dicionário com os
            atributos dos vizinhos quando dados=True.
    
        Levanta
        -------
        ValueError
            Se o nó informado não existir no grafo.
        """

        if no not in self.G:
            raise ValueError(f"O nó {no} não existe no grafo.")

        vizinhos = list(self.G.neighbors(no))

        if dados:
            return {
                vizinho: dict(self.G.nodes[vizinho])
                for vizinho in vizinhos
            }

        return vizinhos