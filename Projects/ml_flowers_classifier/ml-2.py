# https://www.youtube.com/playlist?list=PLOU2XLYxmsIIuiBfYad6rFYQU_jL2ryal
# Use open source data
# Use libs for visualization
# Generate illustrations
# View decision tree
import numpy as np
import graphviz
from sklearn.datasets import load_iris
from sklearn import tree
import graphviz 

iris = load_iris()

print(iris.feature_names)
print(iris.target_names)
print(iris.data[0])
print(iris.target[0])

# for i in range(len(iris.target)):
  # print("Example %d: label %s, features %s" % (i, iris.target[i], iris.data[i]))

test_idx = [0,50,100]

# Training data
train_target = np.delete(iris.target,test_idx)
train_data = np.delete(iris.data,test_idx,axis=0)

# Testing Data
test_target = iris.target[test_idx]
test_data = iris.data[test_idx]

# Train classifier
clf = tree.DecisionTreeClassifier()
clf = clf.fit(train_data, train_target)

# Generate visualization
dot_data = tree.export_graphviz(clf, out_file=None) 
graph = graphviz.Source(dot_data) 
graph.render("iris") 


# Generate visualization 2
dot_data = tree.export_graphviz(clf, out_file=None, 
                     feature_names=iris.feature_names,  
                     class_names=iris.target_names,  
                     filled=True, rounded=True,  
                     special_characters=True)  
graph = graphviz.Source(dot_data)  
graph.render("iris-2") 

# print (test_data[1], test_target[1])
print (test_data[0], test_target[0])
print (test_data[1], test_target[1])
print (test_data[2], test_target[2])

# Questions must be about a feature