import networkx as nx
import matplotlib.pyplot as plt
from IPython.display import Image, display

def draw_graph(Graph: dict, title: str, is_directed: bool = False):
    if is_directed:
        G = nx.DiGraph(Graph)
    else:
        G = nx.Graph(Graph)
    
    plt.figure(figsize=(8, 5)) 
    plt.title(title.upper(), fontsize=14)  

    # Define layout
    pos = nx.circular_layout(G)
    

    if is_directed:
        nx.draw(G, pos, with_labels=True, node_size=300, 
                node_color='black', font_size=12, 
                font_weight='bold', arrows=True, 
                arrowsize=15,
                font_color='white')
    else:
        nx.draw(G, pos, with_labels=True, node_size=300,  
                node_color='black', font_size=12,  #
                font_weight='bold', style='solid', 
                font_color='white')


    plt.savefig('graph_plot.png', format='png')
    plt.close() 

    display(Image(filename='graph_plot.png'))

