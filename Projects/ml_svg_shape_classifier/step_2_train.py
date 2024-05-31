import os
import pickle
import sys
import cv2
import keras
import numpy as np
from PIL import Image
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Dense, Dropout, Flatten
from keras.models import Sequential
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
import tensorflow as tf

from shared.utils import create_log_file, CustomLoggerCallback
from shared.image import preprocess_image

sys.path.append('../')

svg_directory = "./train"

folder = "./pngs"
model_name = 'cnn_shape_predictor.keras'
folder = "./pngs-short"
model_name = 'cnn_shape_predictor-short.keras'
[file_handler, logger] = create_log_file()

def load_images_from_folder():
    images = []
    labels = []
    svg_png_mapping = {}
    for root, _, filenames in os.walk(folder):
        print(f'filenames: {filenames}')
        for filename in filenames:
            print(f'filename: {filename}')
            if filename.lower().endswith('.png'):
                img_path = os.path.join(root, filename)
                img = cv2.imread(img_path)
                if img is not None:
                    preprocessed_img = preprocess_image(img)
                    images.append(preprocessed_img)
                    svg_filename = filename[:-4] + '.svg'
                    svg_png_mapping[svg_filename] = filename
                    svg_type = os.path.basename(os.path.dirname(img_path))
                    print(f'svg_type {svg_type}')
                    labels.append(svg_type)
    return images, labels, svg_png_mapping

def prepare_dataset():
    images, labels, svg_png_mapping = load_images_from_folder()
    images = np.array(images)
    labels = []

    for img_path in svg_png_mapping.values():
        svg_type = os.path.basename(os.path.dirname(img_path))
        labels.append(svg_type)
    
    shape_labels = [
        'cylinder',
        'square',
        'circle',
        'triangle',
        'cube',
        'sphere',
        'pyramid',
    ]
    class_to_shape_mapping = {label_idx: shape_label for label_idx, shape_label in enumerate(shape_labels)}
    labels = np.array(labels)
    unique_labels = list(set(labels))
    label_to_num = {label: idx for idx, label in enumerate(unique_labels)}
    labels = np.array([label_to_num[label] for label in labels])
    x_train, x_test, y_train, y_test = train_test_split(images, labels, test_size=0.2, random_state=42)
    logger.info(f"Number of training samples: {len(x_train)}")
    logger.info(f"Number of test samples: {len(x_test)}")
    return x_train, x_test, y_train, y_test, svg_png_mapping, class_to_shape_mapping

def train_model_with_convolution_neural_networks():
    logger.info('train_model_with_convolution_neural_networks')
    epochs = 12
    batch_size = 128
    num_classes = 10
    x_train, x_test, y_train, y_test, svg_png_mapping, class_to_shape_mapping = prepare_dataset()

    logger.info('Shape of x_train before reshaping: %s', x_train.shape)
    logger.info('Shape of x_test before reshaping: %s', x_test.shape)

    x_train = x_train.reshape(-1, 28, 28, 3).astype('float32') / 255.0
    x_test = x_test.reshape(-1, 28, 28, 3).astype('float32') / 255.0
    logger.info('Shape of x_train after reshaping: %s', x_train.shape)
    logger.info('Shape of x_test after reshaping: %s', x_test.shape)

    y_train = keras.utils.to_categorical(y_train, num_classes)
    y_test = keras.utils.to_categorical(y_test, num_classes)

    
    model = Sequential()
    model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(28, 28, 3)))
    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))
    model.add(Flatten())
    model.add(Dense(128, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(num_classes, activation='softmax'))
    
    model.compile(loss=keras.losses.categorical_crossentropy, optimizer=keras.optimizers.Adadelta(), metrics=['accuracy'])

    checkpoint_path = "checkpoints/cp-{epoch:04d}.weights.h5"
    checkpoint_dir = os.path.dirname(checkpoint_path)
    cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_path, save_weights_only=True, verbose=1)

    if not os.path.exists(checkpoint_dir):
        os.makedirs(checkpoint_dir)

    logger.info('Starting training...')
    logger.info('Shape of x_train before reshaping: %s', x_train.shape)

    custom_logger_callback = CustomLoggerCallback(logger)

    model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, verbose=1, validation_data=(x_test, y_test), callbacks=[cp_callback,custom_logger_callback])

    logger.info('Training completed!')

    score = model.evaluate(x_test, y_test, verbose=0)

    with open('./class_to_shape_mapping.pkl', 'wb') as f:
        pickle.dump(class_to_shape_mapping, f)
    keras.models.save_model(model, model_name)

    logger.info('Test accuracy: %f', score[1])
    logger.info('Test loss: %f, Test accuracy: %f', score[0], score[1])
    file_handler.close()


train_model_with_convolution_neural_networks()