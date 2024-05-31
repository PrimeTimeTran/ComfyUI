import cv2
import cairosvg

def load_image(image_path):
    try:
        with open(image_path, 'r') as f:
            image_data = f.read()
        return image_data
    except Exception as e:
        print("Error occurred during image loading:", e)
        return None

def image_resize(image, width=None, height=None, inter=cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]
    if width is None and height is None:
        return image
    
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))

    resized = cv2.resize(image, dim, interpolation=inter)
    # print(f'resized {resized.shape[0]}')
    # print(f'resized {resized.shape[1]}')
    
    if height is not None and resized.shape[0] < height:
        pad_top = (height - resized.shape[0]) // 2
        pad_bottom = height - resized.shape[0] - pad_top
        resized = cv2.copyMakeBorder(resized, pad_top, pad_bottom, 0, 0, cv2.BORDER_CONSTANT, value=(0, 0, 0))
    
    return resized

def preprocess_image(image):
    if image is not None:
        resized_image = image_resize(image, 28, 28)
        resized_image = resized_image.astype('float32') / 255.0
        return resized_image

def render_svg_to_png(svg_file, png_file):
    with open(svg_file, 'r') as f:
        svg_data = f.read()
    cairosvg.svg2png(bytestring=svg_data, write_to=png_file)
    return png_file
