import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation
fig, ax = plt.subplots(figsize=(6, 4))


class GraphUtils:
    def __init__(self, edges, weighted, directed) -> None:
        self.weighted = weighted
        self.directed = directed
        self.G = nx.DiGraph() if (directed == True) else nx.Graph()
        if (weighted):
            self.G.add_weighted_edges_from(edges)
        else:
            self.G.add_edge(edges)

    def show(self):
        def update(num):
            print('num', num)
            labels = nx.get_edge_attributes(self.G, 'weight')

            pos = nx.spring_layout(self.G, seed=7)

            nx.draw_networkx_nodes(self.G, pos, node_size=500,
                                   node_color='white', linewidths=1, edgecolors='black')
            nx.draw_networkx_edges(
                self.G, pos, alpha=0.5, width=1, min_source_margin=10, min_target_margin=10, arrows=True, connectionstyle='arc3'
            )
            nx.draw_networkx_labels(self.G, pos, font_size=14,
                                    font_family="sans-serif", )

            nx.draw_networkx_edge_labels(self.G, pos=pos, edge_labels=labels)
            # nx.draw_networkx(G, pos, **options)

            # Set margins for the axes so that nodes aren't clipped
            # ax = plt.gca()
            # ax.margins(0.3)
            ax.set_xticks([])
            ax.set_yticks([])

        ani = animation.FuncAnimation(
            fig, update, interval=1000, repeat=True)
        # plt.axis("off")
        # plt.tight_layout()
        # self.update()
        plt.show()


graph = GraphUtils([[2, 1, 1], [2, 3, 1], [3, 4, 1]], True, True)

graph.show()
