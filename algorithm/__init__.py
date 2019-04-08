# "Interface" Algorithm
from abc import ABCMeta, abstractmethod
from graph import Graph

__author__ = 'Flávio José Mendes Coelho'


class Algorithm:
    __metaclass__ = ABCMeta

    @abstractmethod
    def run(self, g: Graph, MAX_ITERATIONS: int):
          pass






