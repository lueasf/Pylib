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
# print(df.head(5))

d = {"no": 0, "yes": 1}
df["y"] = df["y"].map(d) # remplace les valeurs de la colonne y par 0 et 1 pour les additionner

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


### Créer des histogrammes avec Seaborn
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
# plt.show()


### Créer des histogrammes avec plotly.js

# Ce premier graphique affiche 2 courbes (Attracted by Age)
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
plot(fig)

#  Ce second graphique affiche 2 barres (Attracted by Months)
month_index = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
month_df = (
    df.groupby("month")[["y"]]
    .sum().join(df.groupby("month")[["y"]].count(), rsuffix='_count')
).reindex(month_index)
month_df.columns = ["Attracted", "Total Number"]

trace3 = go.Bar(x=month_df.index, y=month_df["Attracted"], name="Attracted")
trace4 = go.Bar(x=month_df.index, y=month_df["Total Number"], name="Total Number")

data2 = [trace3, trace4]
layout2 = {"title": "Share of months"}
fig2 = go.Figure(data=data2, layout=layout2)
plot(fig2, show_link=False)