import networkx as nx
import matplotlib.pyplot as plt
from typing import Dict, List, Callable, Any
import random
import networkx as nx
import matplotlib.pyplot as plt
from typing import Dict, List, Tuple

def classify_edges(G: nx.Graph) -> Dict[Tuple[int, int], str]:
    edge_colors: Dict[Tuple[int, int], str] = {}
    state: Dict[int, int] = {}
    parent: Dict[int, int] = {}
    discovery_time: Dict[int, int] = {}
    time: List[int] = [0]  # Tracks the time during DFS

    # Node states
    NOT_DISCOVERED, IN_PROCESS, DISCOVERED = 0, 1, 2

    def dfs(v: int) -> None:
        state[v] = IN_PROCESS
        discovery_time[v] = time[0]
        time[0] += 1

        for neighbor in G.neighbors(v):
            neighbor_state = state.get(neighbor, NOT_DISCOVERED)
            if neighbor_state == NOT_DISCOVERED:
                parent[neighbor] = v
                edge_colors[(v, neighbor)] = 'blue'  # Tree edge
                dfs(neighbor)
            elif neighbor_state == IN_PROCESS:
                edge_colors[(v, neighbor)] = 'gray'  # Back edge
            elif neighbor_state == DISCOVERED:
                if discovery_time[v] < discovery_time[neighbor]:
                    edge_colors[(v, neighbor)] = 'red'  # Forward edge
                else:
                    edge_colors[(v, neighbor)] = 'orange'  # Cross edge

        state[v] = DISCOVERED

    # Run DFS from every unvisited node to ensure all components are covered
    for node in G.nodes():
        if state.get(node, NOT_DISCOVERED) == NOT_DISCOVERED:
            dfs(node)

    return edge_colors


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
