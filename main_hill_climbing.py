import networkx as nx
import matplotlib.pyplot as plt
from graph import Graph
import heuristics
import algorithm
from mh_hillclimbing import HillClimbing
import util
import time


def testa_HillClimbing_tweak():
    g = Graph(4)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 0)
    g.add_edge(0, 2)
    g.set_color_vertex(0, 0)
    g.set_color_vertex(1, 0)
    g.set_color_vertex(2, 0)
    g.set_color_vertex(3, 0)
    h = g.copy
    print("coloração (antes):", h.get_coloring())
    print("---------------------")
    HillClimbing.tweak(h)
    print("coloração (depois):", h.get_coloring())

    nxg = nx.Graph()
    nxg.add_nodes_from(h.get_vertices())
    nxg.add_edges_from(h.get_edges())

    options = {
        # 'node_color': '#afeeef',
        'edge_color': 'black',
        'with_labels': True,
        'node_size': 400,
        'width': 1}
        # 'alpha': 0.5}
    plt.subplot(121)
    nx.draw(nxg, node_color=h.get_coloring_RBG(), **options)
    plt.show()
    print("done")


def testa_HillClimbing_1():
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 0)
    g.add_edge(0, 2)
    g.add_edge(0, 4)
    g.add_edge(4, 1)
    g.set_color_vertex(0, 0)
    g.set_color_vertex(1, 1)
    g.set_color_vertex(2, 2)
    g.set_color_vertex(3, 3)
    g.set_color_vertex(4, 4)
    h = g.copy
    print("coloração (antes):", h.get_coloring(), " #cores: ", h.number_of_colors())
    HillClimbing.run(h, 5)
    print("---------------------")
    print("coloração (depois):", h.get_coloring(), " #cores: ", h.number_of_colors())

    nxg = nx.Graph()
    nxg.add_nodes_from(h.get_vertices())
    nxg.add_edges_from(h.get_edges())

    options = {
        # 'node_color': '#afeeef',
        'edge_color': 'black',
        'with_labels': True,
        'node_size': 400,
        'width': 1}
        # 'alpha': 0.5}
    plt.subplot(121)
    nx.draw(nxg, node_color=h.get_coloring_RBG(), **options)
    plt.show()
    print("done")


# Testando carga entre Graph e NXGraph, e também quality negativo
def testa_HillClimbing_2():
    NUM_EXPERIMENTS = 1
    nxg_lst = []
    for i in range(NUM_EXPERIMENTS):
        nxg = nx.erdos_renyi_graph(250, 0.20)
        nxg_lst.append(nxg)
        h = util.graph_from_NXGraph(nxg)
        HillClimbing.run(h, MAX_ITERATIONS = 5)

    print("*** done ***")


def testa_HillClimbing_3():
    file_names = ['DSJC125.1.col.txt', 'DSJC125.5.col.txt', 'DSJC125.9.col.txt']
    print("HillClimbing: MAX_ITERATIONS = 5000")
    for file_name in file_names:
        print("---------------------")
        print("file:", file_name)
        print("---------------------")
        inicio = time.time()
        g = readGraphFromFile(file_name)
        best = HillClimbing.run(g, MAX_ITERATIONS = 5000)
        fim = time.time()
        print("tempo:", fim - inicio)
        print("#cores: ", best.number_of_colors())
        print()


def readGraphFromFile(file_name):
    # print("Carregando... ", file_name)
    f = open(file_name, 'r')
    num_vertices = int(f.readline())
    g = Graph(num_vertices)
    for line in f:
        edge_lst = line.split(' ')
        u, v = int(edge_lst[0]), int(edge_lst[1])
        u -= 1
        v -= 1
        g.add_edge(u, v)
    return g


def main():
    testa_HillClimbing_3()
    print("*** done ***")

main()
