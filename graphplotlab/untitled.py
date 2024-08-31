import random
import networkx as nx
import matplotlib.pyplot as plt
from typing import Dict, List, Tuple
def draw_edge_types(Graph: Dict[int, List[int]], title: str, is_directed: bool = False) -> None:
    G = nx.DiGraph(Graph) if is_directed else nx.Graph(Graph)
    pos = nx.circular_layout(G)  # Layout for visual representation
    plt.title(title.upper(), fontsize=16)

    if is_directed:
        edge_colors = classify_edges(G)
        nx.draw(G, pos, with_labels=True, node_size=500, node_color='black', font_size=16,
                font_weight='bold', font_color='white',
                edge_color=[edge_colors.get(edge, 'black') for edge in G.edges()],
                arrows=True, arrowsize=20, connectionstyle='arc3,rad=0.1')

        plt.legend(handles=[
            plt.Line2D([0], [0], color='blue', lw=2, label='Tree Edge'),
            plt.Line2D([0], [0], color='gray', lw=2, label='Back Edge'),
            plt.Line2D([0], [0], color='red', lw=2, label='Forward Edge'),
            plt.Line2D([0], [0], color='orange', lw=2, label='Cross Edge'),
        ], loc='upper left', bbox_to_anchor=(1, 1))
    else:
        nx.draw(G, pos, with_labels=True, node_size=500, node_color='black', font_size=16,
                font_weight='bold', style='solid', font_color='white')

    plt.show()