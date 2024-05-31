import os

from shared.image import render_svg_to_png

def get_files_in_directory(directory):
    files = []
    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            filepath = os.path.join(root, filename)
            files.append(filepath)
    return files

def render_pngs():
    shapes = "./train"
    output_dir = "./pngs"
    files = get_files_in_directory(shapes)
    for f in files:
        relative_path = os.path.relpath(f, shapes)
        output_path = os.path.join(output_dir, os.path.splitext(relative_path)[0] + '.png')
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        render_svg_to_png(f, output_path)

