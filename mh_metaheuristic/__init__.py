import networkx as nx
from algorithm import Algorithm
from heuristics import ColoringHeuristic
from graph import Graph
from heuristic_dsatur import Dsatur

__author__ = 'Flávio José Mendes Coelho'


class Metaheuristic(Algorithm):

    def __init__(self) -> None:
        pass


    @staticmethod
    def initialize(g: Graph) -> Graph:
        pass


    @staticmethod
    def tweak(g: Graph) -> Graph:
        pass

    @staticmethod
    def quality(g: Graph) -> int:
        pass


    @staticmethod
    def run(g: Graph, MAX_ITERATIONS: int):
        pass


    @staticmethod
    def run(g: Graph, MAX_ITERATIONS: int, DECREASE: int):
        pass


    @staticmethod
    def idealSolution(g: Graph) -> bool:
        """
        retorna True se g for uma solução ideal, ou False em c.c.
        Neste caso para um g qualquer o ideal é quality(g) <= 4,
         isto é, se o número de cores de g for igual a 4 devido
         ao teorema das 4 cores, ou menor, no caso de um grafo
         que aceite menos cores (ex. caminho ou ciclo).
        :param g:
        :return: bool
        """
        num_colors = g.number_of_colors()
        return num_colors <= 4
