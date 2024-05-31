
import os
from shapes import generate_shape

from files import render_pngs
shapes = [
    'cylinder',
    'square',
    'circle',
    'triangle',
    'cube',
    'sphere',
    'pyramid',
]

def make_directory(name):
    if not os.path.exists(name):
        os.mkdir(name)

def make_directories(root_dir):
    make_directory(root_dir)
    for shape in shapes:
        shape_dir = os.path.join(root_dir, shape)
        os.makedirs(shape_dir, exist_ok=True)

def generate_files():
    make_directory('checkpoints')
    make_directory('manual-pngs')
    make_directory('manual-testing')
    make_directories('train')
    make_directories('pngs')
    if True:
        for idx, shape in enumerate(shapes):
            for i in range(128):
                generate_shape(i, shape)

            print(f'Generate Shape {shape}: Done')
    print('Generate SVGs: Done')
    print('Generating PNGS...')
    render_pngs()

generate_files()
