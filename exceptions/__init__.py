#Exceções do projeto

__author__ = 'Flávio José Mendes Coelho'


class PopulationFullException(Exception):
    pass


class PopulationEmptyException(Exception):
    pass


class NonProperColoringException(Exception):
    pass


class QueueFullException(Exception):
    pass


class QueueEmptyException(Exception):
    pass


class ColorException(Exception):
    """Exceção geral para cores"""
    pass


class InvalidColorException(ColorException):
    """Cor negativa"""
    pass


class VertexException(Exception):
    """Exceção geral para vértices"""
    pass


class InvalidVertexException(Exception):
    """Vértices inválidos (negativos)"""
    pass


class InvalidKeyException(Exception):
    """Chave inválida"""
    pass
