import networkx as nx
from graph import Graph
import heuristics
import algorithm
from heuristic_dsatur import Dsatur

def main_testa_dsatur1():
    g = Graph(4)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 0)
    g.add_edge(0, 2)
    g.set_color_vertex(0, 0)
    g.set_color_vertex(1, 1)
    g.set_color_vertex(2, 2)
    g.set_color_vertex(3, 1)
    Dsatur.run(g)


def main_testa_random_graphs(g: Graph, N: int):
    for i in range(N):
        nxg = nx.Graph()
        nxg.add_nodes_from(g.get_vertices())
        nxg.add_edges_from(g.get_edges())
        # Usa NX para obter uma coloração randomica gulosa
        NX_coloring = nx.coloring.greedy_color(nxg, strategy=nx.coloring.strategy_saturation_largest_first)
        g.set_coloring_from_NX(NX_coloring)
        print(i)
        if not g.isProperlyColored():
            raise NonProperColoringException("COLORAÇÃO IMPRÓPRIA.")


def main():
    g = Graph(50)
    main_testa_random_graphs(g, 200)


main()