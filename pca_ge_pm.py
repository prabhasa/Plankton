__author__ = 'prabhasa.ravikirthi'

import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.decomposition import PCA

icfile="C:\\Users\\prabhasa.ravikirthi\\Desktop\\Client\\TCAL_PredictiveModelling\\TBOS_proj_2_pred_models\\Ricerca_IC50s_for_compounds_X_and_Y.txt"
ic=pd.read_csv(icfile,sep="\t",header=0,index_col=0)
ic['compound_X'].

gefile="C:\\Users\\prabhasa.ravikirthi\\Desktop\\Client\\TCAL_PredictiveModelling\\TBOS_proj_2_pred_models\\baseline_gene_expression_for_model_training.txt"
ge=pd.read_csv(gefile,sep="\t",header=0,index_col=0)
ge=ge.transpose()

X_reduced = PCA(n_components=3).fit_transform(ge)

fig = plt.figure(1, figsize=(8, 6))
ax = Axes3D(fig, elev=-150, azim=110)
ax.scatter(X_reduced[:, 0], X_reduced[:, 1], X_reduced[:, 2],
           cmap=plt.cm.Paired)
ax.set_title("First three PCA directions")
ax.set_xlabel("1st eigenvector")
ax.w_xaxis.set_ticklabels([])
ax.set_ylabel("2nd eigenvector")
ax.w_yaxis.set_ticklabels([])
ax.set_zlabel("3rd eigenvector")
ax.w_zaxis.set_ticklabels([])

plt.show()
