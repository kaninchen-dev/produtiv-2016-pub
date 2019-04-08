import networkx as nx
import matplotlib.pyplot as plt
import util
import time
import random
import ds_queue
from graph import Graph
import exceptions
import heuristics
import algorithm
from mh_ILS import IteratedLocalSearch


def generateParcialTimes(start: float, stop: float,
                         parcial_times_queue: ds_queue.Queue):
    total_time = 0.0
    while not parcial_times_queue.full():
        parcial_time = random.randrange(start, stop)
        total_time += parcial_time
        try:
            parcial_times_queue.enqueue(parcial_time)
        except exceptions.QueueFullException:
            break
    return total_time

def testa_IteratedLocalSearch_1():
    file_names = ['DSJC125.1.col.txt', 'DSJC125.5.col.txt', 'DSJC125.9.col.txt']
    for file_name in file_names:
        print("---------------------")
        print("file:", file_name)
        print("---------------------")
        inicio = time.time()
        g = readGraphFromFile(file_name)
        MAX_TAM_QUEUE = 10
        parcial_times_queue = ds_queue.Queue(MAX_TAM_QUEUE)
        start, stop = 10, 20
        TOTAL_TIME = generateParcialTimes(start, stop, parcial_times_queue)
        best = IteratedLocalSearch.run(g, parcial_times_queue, TOTAL_TIME)
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
    testa_IteratedLocalSearch_1()
    print("*** done ***")

main()


