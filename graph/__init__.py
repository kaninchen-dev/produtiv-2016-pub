from exceptions import InvalidColorException, InvalidVertexException
import networkx as nx
import matplotlib.pyplot as plt
import colors

__author__ = 'Flávio José Mendes Coelho'


# Grafo simples e não direcionado
class Graph(object):

    def __init__(self, n: int) -> None:
        self.n = n  # ordem
        self.m = 0  # tamanho
        self.vertices = list(range(n))
        self.edges = [] # to-do: substituir def get_edges(self)
        self.adj = [[] for i in range(n)]  # lista de adjacência

        # Coloração (cores dos vértices).
        # O grafo inicia com uma coloração imprópria, ou seja, todos os vértices
        # pintados com uma mesma cor, a cor 0.
        self.coloring = [0 for i in range(n)]


    def set_color_vertex(self, v: int, color) -> None:
        """
        Pinta um vértice com uma cor
        :param v: vértice int
        :type color: int que representa uma cor
        """
        if color < 0 or color > self.n - 1:
            raise InvalidColorException("Cor inválida.")
        if v < 0 or v > self.n - 1:
            raise InvalidVertexException("Vértice inválido.")
        self.coloring[v] = color


    def get_coloring(self) -> list:
        """
        Retorna coloração
        """
        return self.coloring


    def add_edge(self, u, v):
        """
        Adiciona uma aresta
        :param v: vértice int
        :param u: vértice int
        """
        if u < 0 or u > self.n - 1 or v < 0 or v > self.n - 1:
            raise InvalidVertexException("Vértice inválido.")
        self.adj[u].append(v)
        self.adj[v].append(u)
        self.m += 1
        self.edges.append((u, v))


    def adj(self, v: int) -> list:
        """
        Retorna a lista de adjacência de um vértice
        :param v: vértice int
        """
        if v < 0 or v > self.n - 1:
            raise InvalidVertexException("Vértice inválido.")
        return self.adj[v]


    def get_vertices(self):
        return self.vertices


    def get_edges(self):
        """
        Retorna a lista arestas
        """
        edges = []
        for u in range(len(self.adj)):
            list_adj = self.adj[u]
            for v in list_adj:
                edge = (u, v)
                edge_inv = (v, u)
                if edge_inv not in edges:
                    edges.append(edge)
        return edges


    def show_adj(self):
        """
        Imprime a lista de adjacência do grafo
        """
        i = 0
        for l in self.adj:
            print("%d,%d:" % (i, self.coloring[i]), l)
            i += 1


    def get_coloring_RBG(self) -> list:
        """
        Retorna coloração
        """
        coloring_RGB = []
        for cor in self.coloring:
            coloring_RGB.append(colors.get_colors_RBG()[cor])
        return coloring_RGB


    @property
    def copy(self):
        g = Graph(self.n)
        g.m = self.m
        g.adj = self.adj.copy()
        g.coloring = self.coloring.copy()
        return g



    def number_of_colors(self) -> int:
        """
        Obtem o número de cores usadas. Note que
        util.max_value(self.coloring) é somado com 1, pois
        uma cor k está em 0 <= k <= n-1. Logo,
        se as cores 0, 1, ..., k foram escolhidas
        o valor k + 1 indica o número de cores utilizadas. Daí
        o porque de determinarmos o valor máximo de 0..k.
        """
        return self.__max_value(self.coloring) + 1


    def __max_value(self, lst: list) -> int:
        """
        Retorna o valor máximo da lista lst
        :return int:
        """
        max_item = lst[0]
        for item in lst:
            if item > max_item:
                max_item = item
        return max_item


    def set_coloring_from_NX(self, NX_coloring: dict):
        for vertice, color in NX_coloring.items():
            self.coloring[vertice] = color


    def color(self, vertice: int) -> int:
        return self.coloring[vertice]


    def isProperlyColored(self):
        for edge in self.edges:
            u, v = edge
            if self.color(u) == self.color(v):
                return False
        return True


