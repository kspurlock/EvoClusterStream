import pandas as pd
import numpy as np

from evoclusterstream.cluster import EvoDBSCAN
from evoclusterstream.cluster import EvoLouvain
from evoclusterstream.stream import TweepyStreamer

if __name__ == "__main__":
    df = pd.read_csv(r"test_dataset.csv")
    # Take the first 1200 rows of the data with the lat, long, and time columns
    X = df.iloc[:100,[3,4,5]] 
    t_labels = np.unique(X['Time'])

    beta = np.sqrt(np.var(X, axis = 0)[0]) # Latitudinal SD, i.e. beta = 6
    path = ""
    
    ##########################################################################
    # Evolutionary DBSCAN Examples
    ##########################################################################
    
    # Completely static DBSCAN, generations not considered
    evo1 = EvoDBSCAN(min_samples = 2)
    evo1.callSTATIC(X, beta)
    
    # Evolutionary a = 0
    evo2 = EvoDBSCAN(min_samples = 2)
    noise0 = evo2.callDBSCAN(X, t_labels, alpha=0, beta=beta,
                             save_plot=path)
    
    # Evolutionary a = 0.5
    evo3 = EvoDBSCAN(min_samples = 2)
    noise50 = evo3.callDBSCAN(X, t_labels, alpha=0.5, beta=beta,
                              save_plot=path)
    
    # Evolutionary a = 0.8
    evo4 = EvoDBSCAN(min_samples = 2)
    noise50 = evo4.callDBSCAN(X, t_labels, alpha=0.8, beta=beta,
                              save_plot=path)
    
    ##########################################################################
    # Evolutionary Louvain Examples
    ##########################################################################
    
    # Evolutionary a = 0.5
    evo0 = EvoLouvain()
    evo0.callLouvain(X, t_labels, 0, save_plot=path)
    
    # Evolutionary a = 0.8
    evo8 = EvoLouvain()
    evo8.callLouvain(X, t_labels, .8, save_plot=path)
    
    ##########################################################################
    # Stream Example
    ##########################################################################

    search_terms = ['test']
    
    consumer_key = "your_consumer_key"
    consumer_secret_key = "your_consumer_secret_key"

    access_token = "your_access_token"
    access_token_secret = "your_access_token_secret"
    
    Streamer = TweepyStreamer(consumer_key, consumer_secret_key, access_token,
                              access_token_secret)
    
    info = Streamer.stream_tweets(search_terms, n_samples = 10)