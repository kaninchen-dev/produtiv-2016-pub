import networkx as nx
import matplotlib.pyplot as plt
from graph import Graph
import heuristics
import algorithm
from mh_tabu_search import TabuSearch
import util
import time


def testa_TabuSearch_1():
    NUM_EXPERIMENTS = 1
    nxg_lst = []
    for i in range(NUM_EXPERIMENTS):
        nxg = nx.erdos_renyi_graph(100, 0.20)
        nxg_lst.append(nxg)
        h = util.graph_from_NXGraph(nxg)
        TabuSearch.run(h, MAX_ITERATIONS = 8,
                       MAX_LENGTH_TABU_LIST = 20,
                       NUM_TWEAKS = 25)
    print("*** done ***")


def testa_TabuSearch_2():
    file_names = ['DSJC125.1.col.txt', 'DSJC125.5.col.txt', 'DSJC125.9.col.txt']
    print("testa_TabuSearch: MAX_ITERATIONS = 100, MAX_LENGTH_TABU_LIST = 200, NUM_TWEAKS = 250)")
    for file_name in file_names:
        print("---------------------")
        print("file:", file_name)
        print("---------------------")
        inicio = time.time()
        g = readGraphFromFile(file_name)
        best = TabuSearch.run(g, MAX_ITERATIONS = 10,
                       MAX_LENGTH_TABU_LIST = 50,
                       NUM_TWEAKS = 75)
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
    testa_TabuSearch_2()


main()
