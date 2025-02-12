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

pd.set_option("display.precision", 2) # 2 ch après la virgule 
pd.options.display.float_format = '{:.2f}'.format # force l'affichage de 2 ch après la virgule

df = pd.read_csv('bank-additional/bank-additional-full.csv', sep=';')
# print(df.head(5))

d = {"no": 0, "yes": 1}
df["y"] = df["y"].map(d) # remplace les valeurs de la colonne y par 0 et 1

# print(df.columns) affiche les colonnes du dataframe
# print(df.shape) affiche le nombre de lignes et de colonnes du dataframe


### Créer des histogrammes avec matplotlib
df["age"].hist()
plt.title('Distribution of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')

df[["age", "marital"]].groupby(
    "marital"
).mean().plot(kind="bar", rot=45); # affiche la moyenne de l'age par statut marital

df[["age", "job"]].groupby(
    "job"
).mean().plot(kind="bar", rot=45); # affiche la moyenne de l'age par job


### Créer des histogrammes avec seaborn
sns.pairplot(
    df[["age","duration", "marital"]]
);
sns.displot(df.age); # affiche la distribution de l'age

sns.jointplot(x="age", y="duration", data=df, kind="scatter") # affiche un nuage de points

top_jobs = (df.job.value_counts().sort_values(ascending=False).head(10).index.values)
sns.boxplot(y="job", x="age", data=df[df.job.isin(top_jobs)], orient="h") 
'''
df.job.value_counts() compte le nombre de fois que chaque job apparait
puis on trie les jobs par ordre décroissant, en gardant les 10 premiers
.index.values permet de récupérer les noms des jobs
'''

job_marital_y = (df.pivot_table(
    index="job", columns = "marital", values="y", aggfunc="sum")
)
sns.heatmap(job_marital_y, annot=True, fmt="d", linewidths=0.5);
plt.show()


### Créer des histogrammes avec plotly
age_df = (
    df.groupby("age")[["y"]]
    .sum().join(df.groupby("age")[["y"]].count(), rsuffix='_count')
)
age_df.columns = ["Attracted", "Total Number"]
'''
groupby("age")[["y"]] : groupe les données par age et sélectionne la colonne y.
.join() permet de joindre les deux dataframes

Ainsi, cette ligne permet de compter le nombre de personnes attirées par l'offre par age.
'''
trace0 = go.Scatter(x=age_df.index, y=age_df["Attracted"],name="Attracted")
trace1 = go.Scatter(x=age_df.index, y=age_df["Total Number"],name="Total Number")

data = [trace0, trace1]
layout = {"title" : "Statistics of Attracted People by Age"}
fig = go.Figure(data=data, layout=layout)
iplot(fig)
