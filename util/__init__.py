# Implementa rotinas úteis a várias classes
import networkx as nx
import matplotlib.pyplot as plt
import exceptions
from graph import Graph
import heuristics
import algorithm

__author__ = 'Flávio José Mendes Coelho'


def dsatur_hardtocolor_graph() -> Graph:
    g = Graph(7)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    g.add_edge(4, 5)
    g.add_edge(5, 0)
    g.add_edge(1, 5)
    g.add_edge(2, 6)
    g.add_edge(4, 6)
    g.add_edge(3, 6)
    return g


def draw_graph(g: Graph) -> Graph:
    nxg = NXGraph_from_graph(g)
    options = {
        # 'node_color': '#afeeef',
        'edge_color': 'black',
        'with_labels': True,
        'node_size': 400,
        'layout': 'circular_layout',
        # 'layout': 'spring_layout',
        'width': 1}
    # 'alpha': 0.5}
    plt.subplot(121)
    nx.draw(nxg, node_color=g.get_coloring_RBG(), **options)
    plt.show()


def graph_from_NXGraph(nxGraph: nx.Graph()) -> Graph:
    g = Graph(len(nxGraph.nodes()))
    for edge in nxGraph.edges():
        u, v = edge
        g.add_edge(u, v)
    return g


def NXGraph_from_graph(g: Graph) -> nx.Graph:
    nxg = nx.Graph()
    nxg.add_nodes_from(g.get_vertices())
    nxg.add_edges_from(g.get_edges())
    return nxg


