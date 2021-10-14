# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

from evoclusterstream.cluster import EvoDBSCAN
from evoclusterstream.cluster import EvoLouvain

if __name__ == "__main__":

    df = pd.read_csv(r"test_dataset.csv")
    # Take the first 1200 rows of the data with the lat, long, and time columns
    X = df.iloc[:200,[3,4,5]] 
    t_labels = np.unique(X['Time'])

    beta = np.sqrt(np.var(X, axis = 0)[0]) # Latitudinal SD, i.e. beta = 6
    
    ##########################################################################
    # Evolutionary DBSCAN Examples
    ##########################################################################
    
    # Completely static DBSCAN, generations not considered
    evo1 = EvoDBSCAN()
    evo1.callDBSCAN(X, t_labels, alpha=0.8, beta=beta)
    
    evo2 = EvoLouvain()
    evo2.callLouvain(X, t_labels, alpha=0)
