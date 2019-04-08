from exceptions import InvalidColorException, InvalidVertexException
import networkx as nx
import matplotlib.pyplot as plt


__author__ = 'Flávio José Mendes Coelho'


def get_colors_RBG() -> list:
    """
    Retorna lista com 96 cores RGB
    """
    COLORS_RGB = ['#FF00FF', '#FF6347', '#40E0D0', '#A0522D', '#2F4F4F', '#008B8B', '#BA55D3', '#4169E1', '#F0FFF0',
                  '#C0C0C0',
                  '#8B4513', '#9ACD32', '#B0C4DE', '#FFFFF0', '#483D8B', '#D3D3D3', '#F0FFFF', '#FFA07A', '#F4A460',
                  '#6495ED',
                  '#DB7093', '#AFEEEE', '#F0E68C', '#FFB6C1', '#A9A9A9', '#ADD8E6', '#CD853F', '#ADFF2F', '#00BFFF',
                  '#5F9EA0',
                  '#8B0000', '#FF0000', '#C71585', '#808000', '#87CEEB', '#48D1CC', '#DDA0DD', '#DEB887', '#9370DB',
                  '#696969',
                  '#F5F5DC', '#DA70D6', '#F08080', '#DAA520', '#8A2BE2', '#8FBC8F', '#BDB76B', '#B8860B', '#F8F8FF',
                  '#DCDCDC',
                  '#FF69B4', '#D8BFD8', '#FFD700', '#008000', '#8B008B', '#FFEBCD', '#32CD32', '#FFFAF0', '#FFFAFA',
                  '#708090',
                  '#4B0082', '#E0FFFF', '#1E90FF', '#00FFFF', '#FFFF00', '#808080', '#7FFFD4', '#6B8E23', '#F5FFFA',
                  '#7B68EE',
                  '#4682B4', '#E6E6FA', '#B22222', '#00FF7F', '#20B2AA', '#006400', '#0000FF', '#F5F5F5', '#FAEBD7',
                  '#F5DEB3',
                  '#D2691E', '#FFE4C4', '#DC143C', '#FF7F50', '#7FFF00', '#F0F8FF', '#FFA500', '#778899', '#CD5C5C',
                  '#9400D3',
                  '#FF1493', '#66CDAA', '#FF4500', '#90EE90', '#000080', '#BC8F8F']
    return COLORS_RGB


