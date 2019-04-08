import networkx as nx
import numpy
import time
import random
import exceptions
from algorithm import Algorithm
from heuristics import ColoringHeuristic
from mh_metaheuristic import Metaheuristic
from graph import Graph
from heuristic_dsatur import Dsatur
from ds_queue import Queue

__author__ = 'Flávio José Mendes Coelho'


class IteratedLocalSearch(Metaheuristic):

    def __init__(self) -> None:
        pass


    @staticmethod
    def tweak(g: Graph) -> Graph:
        nxg = nx.Graph()
        nxg.add_nodes_from(g.get_vertices())
        nxg.add_edges_from(g.get_edges())
        # Usa NX para obter uma coloração randomica gulosa
        NX_coloring = nx.coloring.greedy_color(nxg,
                                               strategy=nx.coloring.strategy_random_sequential,
                                               interchange=False)
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
    def run(g: Graph, parcial_times_queue: Queue, TOTAL_TIME: float):
        random.seed(37) # número mágico aquieee! :-)
        s = g
        IteratedLocalSearch.initialize(s)  # atribui uma solução inicial
        best = s
        sum_total_time = 0.0
        while sum_total_time < TOTAL_TIME:
            print(".", end="")
            if not parcial_times_queue.empty():
                PARCIAL_TIME = parcial_times_queue.dequeue()
                sum_total_time += PARCIAL_TIME
                inicial_time = time.time()
                currentTime = 0.0
                while currentTime <= PARCIAL_TIME:
                    r = IteratedLocalSearch.tweak(s.copy)
                    qualityR = IteratedLocalSearch.quality(r)
                    qualityS = IteratedLocalSearch.quality(s)
                    if qualityR > qualityS:
                        s = r
                    now_time = time.time()
                    currentTime = now_time - inicial_time

            qualityS = IteratedLocalSearch.quality(s)
            qualityBest = IteratedLocalSearch.quality(best)
            if qualityS > qualityBest:
                    best = s
            s = IteratedLocalSearch.perturb(s.copy)
        print()
        return best



    @staticmethod
    def perturb(g: Graph):
        nxg = nx.Graph()
        nxg.add_nodes_from(g.get_vertices())
        nxg.add_edges_from(g.get_edges())
        # Para tentar "perturbar" a coloração sorteio um método guloso de coloração e
        # aplico uma 'strategy_random_sequential' sobre o grafo obtido.
        strategies = ('connected_sequential', 'connected_sequential_bfs',
                            'connected_sequential_dfs', 'independent_set',
                            'largest_first', 'smallest_last')
        strategy = random.choice(strategies)
        _ = nx.coloring.greedy_color(nxg, strategy, interchange=False)
        NX_coloring = nx.coloring.greedy_color(nxg, strategy='random_sequential', interchange=True)
        g.set_coloring_from_NX(NX_coloring)
        return g

