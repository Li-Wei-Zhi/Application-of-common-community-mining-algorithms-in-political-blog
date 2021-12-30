# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 19:00:21 2021

@author: Lenovo
"""

import networkx as nx
from networkx.algorithms import community #  
import itertools
import matplotlib.pyplot as plt

G = nx.karate_club_graph() # 空手道俱乐部
#G=nx.read_gml(r'C:\Users\Lenovo\Desktop\polblogs.gml')
G=G.to_undirected()
comp = community.girvan_newman(G) # GN算法

k = 3 # 想要4个社区
limited = itertools.takewhile(lambda c: len(c) <= k, comp) # 层次感迭代器
for communities in limited:
    b = list(sorted(c) for c in communities)
    print(b)
#print(b)

pos = nx.spring_layout(G) # 节点的布局为spring型

NodeId = list(G.nodes())
node_size = [G.degree(i)**1.2*90 for i in NodeId] # 节点大小

plt.figure(figsize = (8,6)) # 图片大小
nx.draw(G,pos, with_labels=True)
'''
node_size表示节点大小
node_color表示节点颜色
node_shape表示节点形状
with_labels=True表示节点是否带标签
'''
color_list = ['brown','orange','r','g','b','y','m','gray','black','c','pink']
node_shape = ['s','o','H','D'] 

for i in range(len(b)):
     nx.draw_networkx_nodes(G, pos, node_size=1000,nodelist=b[i], node_color=color_list[i], node_shape=node_shape[i])
    #nx.draw_networkx_nodes(G, pos, nodelist=b[i], node_color=color_list[i])

plt.show()
