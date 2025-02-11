import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
plt.rcParams['figure.figsize'] = (10, 6) # définit la taille des figures

import warnings
warnings.filterwarnings('ignore') # ignore les avertissements

import plotly
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

# pd.set_option("precision", 2) 
pd.options.display.float_format = '{:.2f}'.format 

df = pd.read_csv('bank-additional/bank-additional-full.csv', sep=';')
print(df.head(5))