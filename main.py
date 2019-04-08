import networkx as nx
from graph import Graph
import heuristics
import algorithm
from heuristic_dsatur import Dsatur

def main_testa_dsatur():
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


def main():
    main_testa_dsatur()


main()
