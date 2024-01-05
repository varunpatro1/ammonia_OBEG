import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import geopandas as gpd
from geopandas import GeoDataFrame

def plot_grid_per_depth(df, df_index:int):
    
    titles = ['Jan Depth 1', 'Feb Depth 1', 'Mar Depth 1', \
             'Apr Depth 1', 'May Depth 1', 'Jun Depth 1', \
             'Jul Depth 1', 'Aug Depth 1', 'Sep Depth 1', \
             'Oct Depth 1', 'Nov Depth 1', 'Dec Depth 1']

    fig, ax = plt.subplots(figsize=(20,16), ncols = 3, nrows = 4, gridspec_kw = None)
    countries = gpd.read_file(  
         gpd.datasets.get_path("naturalearth_lowres"))

    for i in range(4):
        for j in range(3): 
            countries.plot(color="lightgrey", ax = ax[i][j])

    indices = [ax[0,0], ax[0,1], ax[0,2], ax[1,0], ax[1,1], ax[1,2], \
               ax[2,0], ax[2,1], ax[2,2], ax[3,0], ax[3,1], ax[3,2]]

    # plot points

    for i in range(12):
        df.plot(x="lon", y="lat", kind="scatter", 
            c=df.iloc[:,i+3], colormap="plasma", 
            title= titles[i] , 
            ax=indices[i])
    plt.show()