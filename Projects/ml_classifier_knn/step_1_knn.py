from shared.utils import setup_save_directory, create_log_file
from shared.mnist_loader import MNIST
import sys
import numpy as np
import os
import pickle
from sklearn import model_selection
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
from matplotlib import style

sys.path.append('../')
style.use('ggplot')
[file_handler, logger] = log_file = create_log_file("summary-knn.log")
save_dir = 'predictions-knn'
setup_save_directory(save_dir)


def load_test_data():
    logger.info('Loading MNIST Data...')
    data = MNIST('./dataset/')

    logger.info('Loading Training Data...')

    img_train, labels_train = data.load_training()
    train_img = np.array(img_train)
    train_labels = np.array(labels_train)

    logger.info('Loading Testing Data...')

    img_test, labels_test = data.load_testing()
    test_img = np.array(img_test)
    test_labels = np.array(labels_test)

    return [train_img, train_labels, test_img, test_labels]


def train_test_split(x, y):
    return model_selection.train_test_split(
        x, y, test_size=0.1)


def create_confusion_matrix(y_test, y_pred, confidence, accuracy):
    logger.info('Creating Confusion Matrix...')
    conf_mat = confusion_matrix(y_test, y_pred)

    logger.info('KNN Trained Classifier Confidence: %f', confidence)
    logger.info('Predicted Values: %f', y_pred)
    logger.info('Accuracy of Classifier on Validation Image Data: %f', accuracy)
    confusion_matrix_str = '\n'.join(['\t'.join(map(str, row)) for row in conf_mat])
    logger.info(f"Confusion Matrix:\n{confusion_matrix_str}")

    plt.matshow(conf_mat)
    plt.title('Confusion Matrix for Validation Data')
    plt.colorbar()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    conf_matrix_filename = os.path.join(
        save_dir, '0-CONFUSION_MATRIX_FOR_VALIDATION_DATA.png')
    plt.savefig(conf_matrix_filename)
    # plt.show()


def make_test_predictions(clf, test_img, test_labels):
    logger.info('Making Predictions on Test Input Images...')
    test_labels_pred = clf.predict(test_img)

    logger.info('Calculating Accuracy of Trained Classifier on Test Data... ')
    acc = accuracy_score(test_labels, test_labels_pred)

    logger.info(' Creating Confusion Matrix for Test Data...')
    conf_mat_test = confusion_matrix(test_labels, test_labels_pred)

    logger.info('Predicted Labels for Test Images: \n%f', test_labels_pred)
    logger.info('Accuracy of Classifier on Test Images: \n%f', acc)
    confusion_matrix_str = '\n'.join(['\t'.join(map(str, row)) for row in conf_mat_test])
    logger.info(f"Confusion Matrix for Test Data:\n{confusion_matrix_str}")


    plt.matshow(conf_mat_test)
    plt.title('Confusion Matrix for Test Data')
    plt.colorbar()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.axis('off')
    conf_matrix_filename = os.path.join(
        save_dir, '0-CONFUSION_MATRIX_FOR_TEST_DATA.png')
    plt.savefig(conf_matrix_filename)
    # plt.show()
    return test_labels_pred


def test_sample_set(test_img, test_labels, test_labels_pred):
    a = np.random.randint(1, 50, 20)
    for idx, i in enumerate(a):
        two_d = (np.reshape(test_img[i], (28, 28)) * 255).astype(np.uint8)
        plt.title('Original Label: {0}  Predicted Label: {1}'.format(
            test_labels[i], test_labels_pred[i]))
        plt.imshow(two_d, interpolation='nearest', cmap='gray')
        filename = os.path.join(
            save_dir, f'{idx}-original-{test_labels[i]}-predict-{test_labels[i]}.png')
        plt.savefig(filename)
        plt.clf()


def k_nearest_neighbors():
    [train_img, train_labels, test_img, test_labels] = load_test_data()
    x_train, x_test, y_train, y_test = train_test_split(
        train_img, train_labels)
    logger.info('Preparing Classifier Training and Validation Data...')

    logger.info(
        'KNN Classifier with n_neighbors = 5, algorithm = auto, n_jobs = 10')
    logger.info('Pickling the Classifier for Future Use...')

    clf = KNeighborsClassifier(n_neighbors=5, algorithm='auto', n_jobs=10)
    clf.fit(x_train, y_train)

    with open('MNIST_KNN.pickle', 'wb') as f:
        pickle.dump(clf, f)

    pickle_in = open('MNIST_KNN.pickle', 'rb')
    clf = pickle.load(pickle_in)

    logger.info('Calculating Accuracy of trained Classifier...')

    confidence = clf.score(x_test, y_test)

    logger.info('Making Predictions on Validation Data...')
    y_pred = clf.predict(x_test)

    logger.info('Calculating Accuracy of Predictions...')
    accuracy = accuracy_score(y_test, y_pred)

    create_confusion_matrix(y_test, y_pred, confidence, accuracy)
    test_labels_pred = make_test_predictions(clf, test_img, test_labels)

    test_sample_set(test_img, test_labels, test_labels_pred)

    logger.info('Done')


k_nearest_neighbors()
