import networkx as nx
import matplotlib.pyplot as plt
from IPython.display import Image, display

def draw_nodes(Graph: dict, title: str):

    G = nx.Graph(Graph)  
    
    plt.figure(figsize=(10, 7))
    plt.title(title.upper(), fontsize=16)
    pos = nx.circular_layout(G)

    # Draw only nodes and labels
    nx.draw_networkx_nodes(G, pos, node_size=500, node_color='darkred')
    nx.draw_networkx_labels(G, pos, font_size=16, font_weight='bold', font_color='white')

    # Save the plot to a file
    plt.savefig('graph_plot.png', format='png')
    plt.close() 

    # Display the plot image
    display(Image(filename='graph_plot.png'))


