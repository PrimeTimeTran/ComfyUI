from sklearn import tree
# Weight & Smoothness
features = [[140,1],[130,1],[150,0],[170,0]]
labels = [0,0,1,1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features,labels)
# Alpha 
# Is what?
# Heavy, bumpy
print (clf.predict([[150,0]]))

# How much training data do we need?
# How does this work in the real world?
# How is the tree created?
# What makes a good feature?

# Decision tree