# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 17:33:04 2021

@author: Lenovo
"""

import networkx as nx
from  fast_unfolding import *
import matplotlib.pyplot as plt
from collections import defaultdict
import random
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

def makeSampleGraph():
    '''
    生成图
    '''
    g = nx.Graph()
    g.add_edge("a", "b", weight=1.)
    g.add_edge("a", "c", weight=1.)
    g.add_edge("b", "c", weight=1.)
    g.add_edge("b", "d", weight=1.)

    return g

def random_Graph():
    '''
    生成随机图
    '''
    g = nx.Graph()

    node_num = random.randint(20,30)

    node_chars = [chr(ord('a')+i) for i in range(node_num)]

    for n in node_chars:
        g.add_node(n)

    for _ in range(node_num*2):
        v = random.sample(node_chars, 2)
        w = 1
        while w==1 or w==0:
            w = round(random.random(), 2)
        g.add_edge(v[0], v[1], weight=w)

    return g

if __name__ == "__main__":
    #sample_graph = makeSampleGraph()
    #sample_graph = random_Graph()
    #sample_graph = nx.karate_club_graph()
    G = nx.read_gml(r'C:\Users\Lenovo\Desktop\polblogs.gml')
    UG=G.to_undirected()
    for node in UG:
        for ngbr in nx.neighbors(UG, node):
            if node in nx.neighbors(UG, ngbr):
                UG.edges[node, ngbr]['weight'] = 1
    print(UG.edges.data('weight'))
    
    louvain = Louvain()
    partition = louvain.getBestPartition(UG)
    color=[]
    p = defaultdict(list)
    colorlist={}
    for node, com_id in partition.items():
        p[com_id].append(node)
        print(node,com_id)
        if com_id in colorlist.keys():
            color.append(colorlist[com_id])
        else:
            colorlist[com_id]=getColor()
            color.append(colorlist[com_id])
    print(len(p.items()))
    for com, nodes in p.items():
        print(com, nodes)
        
    edge_labels=dict([((u,v,),d['weight']) for u,v,d in UG.edges(data=True)])

    pos=nx.spring_layout(UG)
    nx.draw_networkx_edge_labels(UG,pos,edge_labels=edge_labels,node_size=100)
    print(edge_labels)
    nx.draw_networkx(UG,pos,node_color=color)
    plt.show()

