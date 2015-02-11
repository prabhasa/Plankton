__author__ = 'prabhasa.ravikirthi'

from sklearn import datasets
iris = datasets.load_iris()
data = iris.data
print data.shape
# print iris.DESCR

# An example of reshaping data would be the digits dataset
# import pylab as pl
# digits = datasets.load_digits()
# print digits.images.shape
# pl.imshow(digits.images[-1], cmap=pl.cm.gray_r)
# # pl.show()
# data = digits.images.reshape((digits.images.shape[0], -1))

# Estimators objects


