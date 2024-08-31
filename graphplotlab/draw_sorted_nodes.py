import matplotlib.pyplot as plt
from typing import List
import random


def draw_sorted_nodes(nodes : List[int], title:str) -> None:
    num_nodes = len(nodes)

    # Create a figure and a set of subplots
    fig, ax = plt.subplots(figsize=(num_nodes * 2, 2))

    ax.set_xlim(0, num_nodes)
    ax.set_ylim(0, 1)

    ax.axis('off')
    colors= [
        ('red', 'yellow'),
        ('green', 'magenta'),
        ('blue', 'orange'),
        ('orange', 'blue'),
        ('purple', 'cyan'),
        ('cyan', 'purple'),
        ('magenta', 'green'),
        ('yellow', 'red')
    ]
    color = random.choice(colors)
    for i, node in enumerate(nodes):

        circle = plt.Circle((i + 0.5, 0.5), 0.4, color=color[0], fill=True)
        ax.add_artist(circle)

        ax.text(i + 0.5, 0.5, node, ha='center', va='center', fontsize=20, color=color[1], fontweight='bold', )

    ax.set_aspect('equal')
    plt.title(title, fontsize=16)

    plt.show()
