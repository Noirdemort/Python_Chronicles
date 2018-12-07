###!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 24 14:10:10 2018

@author: noirdemort
"""

# simulation of social networks

import numpy as np
import pandas as pd 
import networkx as nx

#from pylab import rcParams
import seaborn as sb
import matplotlib.pyplot as plt


# rcParams["figure.figsize"] = 5,4
# sb.set_style("whitegrid")

sn = nx.gn_graph(7,seed=25)

for line in nx.generate_edgelist(sn,data=False):
    print(line)

sn.node[0]['name'] = "Alpha"
sn.node[1]['name'] = "Bravo"
sn.node[2]['name'] = "Charlie"
sn.node[3]['name'] = "Delta"
sn.node[4]['name'] = "Echo"
sn.node[5]['name'] = "Foxtrot"
sn.node[6]['name'] = "Golf"

sn.add_nodes_from([(0,{'age':25}),(1,{'age':31}),(2,{'age':18}),(3,{'age':37}),(4,{'age':25}),(4,{'age':23}),(5,{'age':45}),(6,{'age':22})])

print(sn.node[0])

sn.node[0]['gender'],sn.node[2]['gender'],sn.node[4]['gender'] = 'f'*3
sn.node[1]['gender'],sn.node[3]['gender'],sn.node[5]['gender'] = 'm'*3

sn.node[1]['gender']

nx.draw_circular(sn,node_color='bisque',with_labels=True)

labeldict ={0:'Alpha',1:'Bravo',2:'Charlie',3:'Delta',4:'Echo',5:'Foxtrot',6:'Golf'}

nx.draw_circular(sn,node_color='bisque',with_labels=True,labels=labeldict)

usn = sn.to_undirected()
nx.draw_spectral(usn,node_color='bisque',with_labels=True,labels=labeldict)
