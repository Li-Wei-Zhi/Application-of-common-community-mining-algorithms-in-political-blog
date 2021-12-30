# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 19:52:14 2021

@author: Lenovo
"""

import networkx as nx
G=nx.read_gml(r'C:\Users\Lenovo\Desktop\polblogs.gml')
UG = G.to_undirected()
print(type(UG))


