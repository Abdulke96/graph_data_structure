import networkx as nx
import matplotlib.pyplot as plt
from typing import Dict, List
import random

def draw_scc(scc_components: List[Dict[int, List[int]]], titles: List[str], is_directed: bool = False) -> None:
    num_components = len(scc_components)
    cols = 2  # Number of columns for subplots
    rows = (num_components + cols - 1) // cols  # Number of rows needed

    fig, axes = plt.subplots(rows, cols, figsize=(15, 5 * rows))
    fig.suptitle("Strongly Connected Components", fontsize=16)

    # Define a set of colors for nodes and labels
    colors = [
        ('red', 'yellow'),
        ('green', 'magenta'),
        ('blue', 'orange'),
        ('orange', 'blue'),
        ('purple', 'cyan'),
        ('cyan', 'purple'),
        ('magenta', 'green'),
        ('yellow', 'red')
    ]
    
    # Flatten axes array for easy iteration
    if num_components == 1:
        axes = [axes]
    else:
        axes = axes.flatten()

    for i, component in enumerate(scc_components):
        ax = axes[i]
        color = random.choice(colors)
        title = titles[i] if i < len(titles) else f"SCC {i + 1}"
        G = nx.DiGraph(component) if is_directed else nx.Graph(component)
        pos = nx.circular_layout(G)

        # Draw graph with increased node size and decreased edge thickness
        nx.draw(G, pos, with_labels=True, node_size=3500,  # Increase node size
                node_color=color[0], font_size=20, font_weight='bold', 
                edge_color='gray',  # Color of edges
                width=0.5,  # Decrease edge thickness
                arrows=True if is_directed else False,
                arrowsize=20 if is_directed else None, font_color=color[1], ax=ax)

        ax.set_title(title)

    # Hide any unused subplots
    for j in range(num_components, len(axes)):
        axes[j].axis('off')

    plt.tight_layout(rect=[0, 0, 1, 0.96])  # Adjust title position
    plt.show()
