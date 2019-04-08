import networkx as nx
from algorithm import Algorithm
from heuristics import ColoringHeuristic
from mh_metaheuristic import Metaheuristic
from graph import Graph
from heuristic_dsatur import Dsatur
from ds_queue import Queue

__author__ = 'Flávio José Mendes Coelho'


class TabuSearch(Metaheuristic):


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
    def initialize(g: Graph) -> Graph:
        Dsatur.run(g) # g sai colorido pelo dsatur da NX



    @staticmethod
    def run(g: Graph, MAX_ITERATIONS: int, MAX_LENGTH_TABU_LIST: int, NUM_TWEAKS: int):
        s = g
        TabuSearch.initialize(s)  # atribui uma solução inicial
        best = s
        tabuQueue = Queue(MAX_LENGTH_TABU_LIST) # "tabu list": fila de soluções já exploradas
        tabuQueue.enqueue(s)
        iterations = 1
        while iterations <= MAX_ITERATIONS:
            if (iterations % 7) == 0:
                print(".", end="")
            if tabuQueue.full():
                tabuQueue.dequeue() # remove solução da fila (solução mais antiga)
            r = TabuSearch.tweak(s.copy)
            for _ in range(NUM_TWEAKS):
                w = TabuSearch.tweak(s.copy)
                qualityW = TabuSearch.quality(w)
                qualityR = TabuSearch.quality(r)
                if (not tabuQueue.in_queue(w)) \
                        and ((qualityW > qualityR) or (tabuQueue.in_queue(r))):
                    r = w
            if not tabuQueue.in_queue(r):
                s = r
                tabuQueue.enqueue(r)
            qualityS = TabuSearch.quality(s)
            qualityBest = TabuSearch.quality(best)
            if qualityS > qualityBest:
                best = s
            iterations += 1
        print()
        return best



