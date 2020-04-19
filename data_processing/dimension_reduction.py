import numpy as np
import csv

from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

import matplotlib.pyplot as plt

X = np.loadtxt('features_data.csv', delimiter=',')
Y = np.loadtxt('labels.csv', delimiter=',')

# PCA-2
pca = PCA(n_components=2)
X_r = pca.fit(X).transform(X)
# np.savetxt('data.csv', X_r1, fmt='%d', delimiter=',')

# TSNE-2
tsne = TSNE(n_components=2)
tsne.fit_transform(X)
X_r2 = tsne.embedding_
# np.savetxt('data.csv', X_r2, fmt='%d', delimiter=',')

# LDA-1
lda = LinearDiscriminantAnalysis(n_components=1)
X_r3 = lda.fit(X, Y).transform(X)
# np.savetxt('data.csv', X_r3, fmt='%d', delimiter=',')

# Percentage of variance explained for each components of PCA
print('explained variance ratio (first two components) of PCA: %s'
      % str(pca.explained_variance_ratio_))

colors = ['navy', 'turquoise']
target_names = ['zaoying', 'chuxue']
lw = 2

# plt for PCA-2
plt.figure()
for color, i, target_name in zip(colors, [0, 1], target_names):
    plt.scatter(X_r[Y == i, 0], X_r[Y == i, 1], color=color, alpha=.8, lw=lw,
                label=target_name)
plt.legend(loc='best', shadow=False, scatterpoints=1)
plt.title('PCA-2')
# plt.savefig('./PCA-2.jpg')

# plt for TSNE-2
plt.figure()
for color, i, target_name in zip(colors, [0, 1], target_names):
    plt.scatter(X_r2[Y == i, 0], X_r2[Y == i, 1], alpha=.8, color=color,
                label=target_name)
plt.legend(loc='best', shadow=False, scatterpoints=1)
plt.title('TSNE-2')
# plt.savefig('./TSNE-2.jpg')

# plt for LDA-1
plt.figure()
for color, i, target_name in zip(colors, [0, 1], target_names):
    plt.scatter(X_r3[Y == i, 0], X_r3[Y == i, 0], alpha=.8, color=color,
                label=target_name)
plt.legend(loc='best', shadow=False, scatterpoints=1)
plt.title('LDA-1')
# plt.savefig('./LDA-1.jpg')

plt.show()
