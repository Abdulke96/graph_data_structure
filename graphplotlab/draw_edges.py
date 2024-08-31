import networkx as nx
import matplotlib.pyplot as plt
from IPython.display import Image, display

def draw_edges(Graph: dict, title: str):
    # Create a NetworkX graph
    G = nx.Graph(Graph)  # This works for both directed and undirected graphs in terms of visualizing edges

    plt.figure(figsize=(10, 7))
    plt.title(title.upper(), fontsize=16)
    pos = nx.circular_layout(G)

    # Draw nodes
    nx.draw_networkx_nodes(G, pos, node_size=500, node_color='white')

    # Draw edges
    nx.draw_networkx_edges(G, pos, edge_color='gray', width=2, style='solid')

    # Draw edge labels
    edge_labels = {(u, v): f'{u}-{v}' for u, v in G.edges()}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='black')

    # Draw node labels
    nx.draw_networkx_labels(G, pos, font_size=16, font_weight='bold', font_color='black')

    # Save the plot to a file
    plt.savefig('graph_edges.png', format='png')
    plt.close() 

    # Display the plot image
    display(Image(filename='graph_edges.png'))

