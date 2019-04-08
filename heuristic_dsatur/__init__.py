import networkx as nx
from graph import Graph
from heuristics import ColoringHeuristic
from algorithm import Algorithm

__author__ = 'Flávio José Mendes Coelho'


class Dsatur(ColoringHeuristic):

    def __init__(self):
        pass

    @staticmethod
    def run(g: Graph):
        h = g.copy
        nxg = nx.Graph()
        nxg.add_nodes_from(h.get_vertices())
        nxg.add_edges_from(h.get_edges())
        NX_coloring = nx.coloring.greedy_color(nxg,
                                               strategy=nx.coloring.strategy_saturation_largest_first)
        g.set_coloring_from_NX(NX_coloring)
        # Verifiquei em 10^8 tentativas que o DSATUR da NX retorna uma
        # coloração própria. Só verifico a coloração aqui somente para
        # mostrar a funcionalidade do método g.isProperlyColored().
        if not g.isProperlyColored():
            raise NonProperColoringException("COLORAÇÃO IMPRÓPRIA.")
