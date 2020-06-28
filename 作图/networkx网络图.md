```python
import networkx as nx
import matplotlib.pyplot as plt


def show(G):
    nx.draw(G, with_labels=True)
    plt.show()


G = nx.Graph()  # 创建无向图
G.add_nodes_from(['a', 'b', 'c'])
G.add_node('d')
G.add_edge('a', 'd')
G.add_edge('b', 'd')
G.add_edge('c', 'd')
show(G)
```