import networkx as nx
from graph import Graph

def testa_coloracao_manual():
    g = Graph(4)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 0)
    g.add_edge(0, 2)
    g.set_color_vertex(0, 0)
    g.set_color_vertex(1, 1)
    g.set_color_vertex(2, 2)
    g.set_color_vertex(3, 1)
    h = g.copy
    h.show_adj()
    print("arestas:", h.get_edges())
    print("coloração:", h.get_coloring())

    nxg = nx.Graph()
    nxg.add_nodes_from(h.get_vertices())
    nxg.add_edges_from(h.get_edges())
    print(nxg.nodes())
    print(nxg.edges())

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


def main():
    testa_coloracao_manual()


#main()
