import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
plt.rcParams['figure.figsize'] = (10, 6) # définit la taille des figures

import warnings
warnings.filterwarnings('ignore') # ignore les avertissements

import plotly
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot

pd.set_option("display.precision", 2) # 2 ch après la virgule 
pd.options.display.float_format = '{:.2f}'.format # force l'affichage de 2 ch après la virgule

df = pd.read_csv('bank-additional/bank-additional-full.csv', sep=';')
d = {"no": 0, "yes": 1}
df["y"] = df["y"].map(d) # remplace les valeurs de la colonne y par 0 et 1 pour les additionner


### Visual Analysis by categories

# with Pandas
# crosstab_marital = pd.crosstab(df["y"], df["marital"])
# print(crosstab_marital)

# with Seaborn 
# build the countplot for the month feature by the y feature target values.
plt.figure()
sns.countplot(x="marital", hue="y", data=df) 
plt.show()

categorical = []
numerical = []