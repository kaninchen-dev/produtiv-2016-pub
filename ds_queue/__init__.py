import exceptions

__author__ = 'Flávio José Mendes Coelho'


# Fila com in_queue()
class Queue(object):

    def __init__(self, MAX_LENGTH):
        self.__MAX_LENGTH = MAX_LENGTH
        self.__items = []

    def enqueue(self, item):
        if not self.full():
            self.__items.append(item)
        else:
            raise exceptions.QueueFullException("Fila cheia.")


    def dequeue(self):
        if not self.empty():
            return self.__items.pop(0) # remove o primeiro da lista
        else:
            raise exceptions.QueueEmptyException("Fila vazia.")


    def length(self):
        return len(self.__items)


    def in_queue(self, it):
        return it in self.__items


    def full(self):
        return len(self.__items) == self.__MAX_LENGTH


    def empty(self):
        return len(self.__items) == 0


    def print(self):
        return print(self.__items)

