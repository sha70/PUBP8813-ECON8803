# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 12:42:22 2019

@author: Susie
"""

import main

test_size=0.2

num_filters = 100
filter_sizes = [3,4,5]
lr = 1e-3 #learning rate
   
l2_constraint = None # None or range of XX
dropout_percent = 0.6 

num_epoch = 3
batch_size = 128


#replication of the paper
# tuning to beat the 84.13%, prec. 87%, rec. 83%
# sample size training vs accuracy
# filter sizes vs accuracy

# 

# print out all the parameters after each run
# a separate script for visualizing 


main
