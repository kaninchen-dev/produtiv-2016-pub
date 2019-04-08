# Interface para heurísticas clássicas para coloração (Dsatur, etc)
from abc import ABCMeta, abstractmethod
from algorithm import Algorithm

__author__ = 'Flávio José Mendes Coelho'


class ColoringHeuristic(Algorithm):
    __metaclass__ = ABCMeta

    @abstractmethod
    def run(self):
          pass



