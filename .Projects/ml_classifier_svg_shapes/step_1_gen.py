
import os
from shapes import generate_shape
from shared.image import render_svg_to_png

shapes = [
    'cylinder',
    'square',
    'circle',
    'triangle',
    'cube',
    'sphere',
    'pyramid',
]


def get_files_in_directory(directory):
    files = []
    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            filepath = os.path.join(root, filename)
            files.append(filepath)
    return files


def render_pngs():
    shapes = "./data/train"
    output_dir = "./data/pngs"
    files = get_files_in_directory(shapes)
    for f in files:
        relative_path = os.path.relpath(f, shapes)
        output_path = os.path.join(
            output_dir, os.path.splitext(relative_path)[0] + '.png')
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        render_svg_to_png(f, output_path)


def make_directory(name):
    if not os.path.exists(name):
        os.mkdir(name)


def make_directories(root_dir):
    make_directory(root_dir)
    for shape in shapes:
        shape_dir = os.path.join(root_dir, shape)
        os.makedirs(shape_dir, exist_ok=True)


def generate_files():
    make_directory('./data/checkpoints')
    make_directory('./data/manual-pngs')
    make_directory('./data/manual-testing')
    make_directories('./data/train')
    make_directories('./data/pngs')
    if True:
        for idx, shape in enumerate(shapes):
            for i in range(128):
                generate_shape(i, shape)

            print(f'Generate Shape {shape}: Done')
    print('Generate SVGs: Done')
    print('Generating PNGS...')
    render_pngs()


generate_files()
