#!/usr/bin/env python3

#found guide and source code here: https://nbviewer.jupyter.org/github/SuperCowPowers/bat/blob/master/notebooks/Anomaly_Detection.ipynb
import bat
from bat import log_to_dataframe
from bat import dataframe_to_matrix
import pandas as pd
import numpy as np
import sklearn
from sklearn.ensemble import IsolationForest
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans


bro_df = log_to_dataframe.LogToDataFrame('~/giant/conn.log')
print('Read in {:d} Rows...'.format(len(bro_df)))
bro_df.head()
