import sys
sys.path.append('./1-knn')
sys.path.append('./2-svm')
sys.path.append('./4-cnn')
from Projects.ml_classifier_knn.step_2_cnn import train_model_with_convolution_neural_networks, use_trained_model
from svm import support_vector_machines
from Projects.ml_classifier_knn.step_1_knn import k_nearest_neighbors

if __name__ == "__main__":
    # k_nearest_neighbors()
    # support_vector_machines()
    train_model_with_convolution_neural_networks()
    # use_trained_model()
