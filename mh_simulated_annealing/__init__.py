import networkx as nx
from algorithm import Algorithm
from heuristics import ColoringHeuristic
from mh_metaheuristic import Metaheuristic
from graph import Graph
from heuristic_dsatur import Dsatur
import math
import random

__author__ = 'Flávio José Mendes Coelho'


class SimulatedAnnealing(Metaheuristic):

    def __init__(self) -> None:
        pass


    @staticmethod
    def tweak(g: Graph) -> Graph:
        nxg = nx.Graph()
        nxg.add_nodes_from(g.get_vertices())
        nxg.add_edges_from(g.get_edges())
        # Usa NX para obter uma coloração randomica gulosa
        NX_coloring = nx.coloring.greedy_color(nxg, strategy=nx.coloring.strategy_random_sequential, interchange=True)
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
    def initialize(g: Graph) -> Graph:
        Dsatur.run(g) # g sai colorido pelo dsatur da NX


    @staticmethod
    def run(g: Graph, MAX_ITERATIONS: int, DECREASE: float):
        temperature = 0.99  # deve iniciar próximo a 1.0
        SimulatedAnnealing.initialize(g)  # atribui uma solução inicial
        best = g
        iterations = 1
        while (temperature > 0.000) and (iterations <= MAX_ITERATIONS):
            if (iterations % 7) == 0:
                print(".", end="")
            h = SimulatedAnnealing.tweak(g.copy)
            qualityH  = SimulatedAnnealing.quality(h)
            qualityG = SimulatedAnnealing.quality(g)
            # Na linda seguinte, qualityH e qualityG precisam ser
            # multiplicadas por -1 pois seus valores são negativos
            # (aqui, "menor" qualidade significa número de cores menor)
            formula_value = SimulatedAnnealing.formula(qualityH*(-1), qualityG*(-1), temperature)
            if qualityH > qualityG \
                or random.random() < formula_value:
                g = h.copy
                qualityG = qualityH
            temperature -= DECREASE
            qualityBest = SimulatedAnnealing.quality(best)
            if qualityG > qualityBest:
                best = g
            iterations += 1
        print()
        return best


    @staticmethod
    def formula(qualityH: int, qualityG: int, temperature: float) -> float:
        """
        Fórmula padrão do Simulated Annealing
        (veja Essentials of Metaheuristics - Sean Luke - 2nd Ed - Ver 2.2, pag. 25).
        De acordo com https://docs.python.org/3/library/math.html
        math.exp(x) é preciso do que math.pow(math.e, x).
        :param qualityH: int
        :param qualityG: int
        :param temperature: float
        :return: float
        """
        return math.exp(float(qualityH - qualityG)/temperature)


