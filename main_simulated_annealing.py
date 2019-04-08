import networkx as nx
import matplotlib.pyplot as plt
from graph import Graph
import heuristics
import algorithm
from mh_simulated_annealing import SimulatedAnnealing
import util
import time


def testa_SimulatedAnnealing_1():
    NUM_EXPERIMENTS = 1
    nxg_lst = []
    for i in range(NUM_EXPERIMENTS):
        nxg = nx.erdos_renyi_graph(250, 0.20)
        nxg_lst.append(nxg)
        h = util.graph_from_NXGraph(nxg)
        SimulatedAnnealing.run(h, MAX_ITERATIONS = 5, DECREASE = 0.03)
    print("*** done ***")


def testa_SimulatedAnnealing_2():
    file_names = ['DSJC125.1.col.txt', 'DSJC125.5.col.txt', 'DSJC125.9.col.txt']
    print("testa_SimulatedAnnealing: MAX_ITERATIONS = 10000")
    for file_name in file_names:
        print("---------------------")
        print("file:", file_name)
        print("---------------------")
        inicio = time.time()
        g = readGraphFromFile(file_name)
        best = SimulatedAnnealing.run(g, MAX_ITERATIONS = 10000, DECREASE = 0.005)
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
    testa_SimulatedAnnealing_2()
    print("*** done ***")

main()