import os
import pickle
import cv2
import keras
import numpy as np

from shared.image import render_svg_to_png,preprocess_image
from files import render_svg_to_png

# model = keras.models.load_model('./cnn_shape_predictor-short.keras')
model = keras.models.load_model('./cnn_shape_predictor.keras')
with open('./class_to_shape_mapping.pkl', 'rb') as f:
    class_to_shape_mapping = pickle.load(f)

def predict_shape(image, metadata=None):
    processed_img = preprocess_image(image)
    processed_img = np.expand_dims(processed_img, axis=0)
    predictions = model.predict(processed_img)
    predicted_class = np.argmax(predictions)
    if metadata:
        print(f'Metadata: {metadata}')
    return class_to_shape_mapping[predicted_class]

def test_files():
    images = []
    svg_labels = {}
    
    # Info: Testing svgs
    for root, _, filenames in os.walk('manual-testing'):
        for filename in filenames:
            img_path = os.path.join(root, filename)

            svg_type = os.path.basename(os.path.dirname(img_path))
            images.append(img_path)
            print(f'img_path {img_path}')
            print(f'svg_type {svg_type}')
            svg_labels[img_path] = svg_type

    for img_path in images:
        name = os.path.splitext(os.path.basename(img_path))[0]
        png_name = f'./manual-pngs/{name}.png'
        render_svg_to_png(img_path, png_name)
        img = cv2.imread(png_name)
        metadata = svg_labels[img_path]
        predicted_class = predict_shape(img, metadata)
        print('Predicted class:', predicted_class)

    # Info: Testing PNGs
    # for root, _, filenames in os.walk('manual-pngs'):
    #     for filename in filenames:
    #         img_path = os.path.join(root, filename)
    #         img = cv2.imread(img_path)
    #         predicted_class = predict_shape(img)
    #         print('Predicted class:', predicted_class)

def print_classes():
    print(class_to_shape_mapping[0])
    print(class_to_shape_mapping[1])
    print(class_to_shape_mapping[2])
    print(class_to_shape_mapping[4])
    print(class_to_shape_mapping[5])
    print(class_to_shape_mapping[6])

print_classes()
# test_files()