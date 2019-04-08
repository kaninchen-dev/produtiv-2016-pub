import networkx as nx
from algorithm import Algorithm
from heuristics import ColoringHeuristic
from mh_metaheuristic import Metaheuristic
from graph import Graph
from heuristic_dsatur import Dsatur

__author__ = 'Flávio José Mendes Coelho'


class HillClimbing(Metaheuristic):

    def __init__(self) -> None:
        pass


    @staticmethod
    def tweak(g: Graph) -> Graph:
        nxg = nx.Graph()
        nxg.add_nodes_from(g.get_vertices())
        nxg.add_edges_from(g.get_edges())
        # Usa NX para obter uma coloração randomica gulosa
        NX_coloring = nx.coloring.greedy_color(nxg, strategy=nx.coloring.strategy_random_sequential,
                                               interchange=True)
        g.set_coloring_from_NX(NX_coloring)
        return g


    @staticmethod
    def quality(g: Graph) -> int:
        """
        Retorna a qualidade da coloração de g.
        No livro Essentials of Metaheuristics - Sean Luke - 2nd Ed - Ver 2.2,
        a qualidade é uma grandeza crescente (maior qualidade, maior valor).
        Porém, como a qualidade em coloração própria clássica está
        relacionada à minimização da coloração, tenho de fornecer uma
        qualidade negativa.
        :param g:
        :return: int
        """
        num_colors = g.number_of_colors()
        return -1*num_colors


    @staticmethod
    def initialize(g: Graph):
        Dsatur.run(g) # g sai colorido pelo dsatur da NX


    @staticmethod
    def run(g: Graph, MAX_ITERATIONS: int):
        HillClimbing.initialize(g)  # atribui uma solução inicial
        iterations = 1
        while (iterations <= MAX_ITERATIONS) and (not HillClimbing.idealSolution(g)):
            if (iterations % 77) == 0:
                print(".", end="")
            h = HillClimbing.tweak(g.copy)
            if HillClimbing.quality(h) > HillClimbing.quality(g):
                g = h.copy
            iterations += 1
        print()
        return g


