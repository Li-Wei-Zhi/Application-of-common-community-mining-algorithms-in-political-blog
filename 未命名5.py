import community
import networkx as nx
import matplotlib.pyplot as plt
import random
#from igraph import *
#better with karate_graph() as defined in networkx example.
#erdos renyi don't have true community structure
G = nx.read_gml(r'C:\Users\Lenovo\Desktop\polblogs.gml')
UG=G.to_undirected()
M =nx.karate_club_graph() # 空手道俱乐部
#first compute the best partition
partition = community.best_partition(UG)#resolution=200


# karate = Nexus.get("karate")
# cl = karate.community_fastgreedy()
# k=2
# cl.as_clustering(k).membership

def getColor():
    color: int
    color1 = random.randint(16, 255)
    color2 = random.randint(16, 255)
    color3 = random.randint(16, 255)
    color1 = hex(color1)
    color2 = hex(color2)
    color3 = hex(color3)
    ans = "#" + color1[2:] + color2[2:] + color3[2:]
    return ans

#drawing
size = float(len(set(partition.values())))
pos = nx.spring_layout(G)
count = 0.
for com in set(partition.values()) :
    count = count + 1.
    color=getColor()
    list_nodes = [nodes for nodes in partition.keys()
                                if partition[nodes] == com]
    nx.draw_networkx_nodes(G, pos, list_nodes, node_size = 50,
                                node_color = color)


nx.draw_networkx_edges(G,pos, alpha=0.1)
plt.show()
