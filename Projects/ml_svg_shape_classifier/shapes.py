import random
import math
import svgwrite
import random

html_named_colors = [
    "AliceBlue", "AntiqueWhite", "Aqua", "Aquamarine", "Azure", "Beige", "Bisque",
    "Black", "BlanchedAlmond", "Blue", "BlueViolet", "Brown", "BurlyWood", "CadetBlue",
    "Chartreuse", "Chocolate", "Coral", "CornflowerBlue", "Cornsilk", "Crimson", "Cyan",
    "DarkBlue", "DarkCyan", "DarkGoldenRod", "DarkGray", "DarkGreen", "DarkKhaki",
    "DarkMagenta", "DarkOliveGreen", "DarkOrange", "DarkOrchid", "DarkRed", "DarkSalmon",
    "DarkSeaGreen", "DarkSlateBlue", "DarkSlateGray", "DarkTurquoise", "DarkViolet",
    "DeepPink", "DeepSkyBlue", "DimGray", "DodgerBlue", "FireBrick", "FloralWhite",
    "ForestGreen", "Fuchsia", "Gainsboro", "GhostWhite", "Gold", "GoldenRod", "Gray",
    "Green", "GreenYellow", "HoneyDew", "HotPink", "IndianRed", "Indigo", "Ivory", "Khaki",
    "Lavender", "LavenderBlush", "LawnGreen", "LemonChiffon", "LightBlue", "LightCoral",
    "LightCyan", "LightGoldenRodYellow", "LightGray", "LightGreen", "LightPink",
    "LightSalmon", "LightSeaGreen", "LightSkyBlue", "LightSlateGray", "LightSteelBlue",
    "LightYellow", "Lime", "LimeGreen", "Linen", "Magenta", "Maroon", "MediumAquaMarine",
    "MediumBlue", "MediumOrchid", "MediumPurple", "MediumSeaGreen", "MediumSlateBlue",
    "MediumSpringGreen", "MediumTurquoise", "MediumVioletRed", "MidnightBlue", "MintCream",
    "MistyRose", "Moccasin", "NavajoWhite", "Navy", "OldLace", "Olive", "OliveDrab",
    "Orange", "OrangeRed", "Orchid", "PaleGoldenRod", "PaleGreen", "PaleTurquoise",
    "PaleVioletRed", "PapayaWhip", "PeachPuff", "Peru", "Pink", "Plum", "PowderBlue",
    "Purple", "RebeccaPurple", "Red", "RosyBrown", "RoyalBlue", "SaddleBrown", "Salmon",
    "SandyBrown", "SeaGreen", "SeaShell", "Sienna", "Silver", "SkyBlue", "SlateBlue",
    "SlateGray", "Snow", "SpringGreen", "SteelBlue", "Tan", "Teal", "Thistle", "Tomato",
    "Turquoise", "Violet", "Wheat", "White", "WhiteSmoke", "Yellow", "YellowGreen"
]

svg_safe = [
    "AliceBlue", "AntiqueWhite", "Aqua", "Aquamarine", "Azure", "Beige", "Bisque",
    "Black", "BlanchedAlmond", "Blue", "BlueViolet", "Brown", "BurlyWood", "CadetBlue",
    "Chartreuse", "Chocolate", "Coral", "CornflowerBlue", "Cornsilk", "Crimson", "Cyan",
    "DarkBlue", "DarkCyan", "DarkGoldenRod", "DarkGray", "DarkGreen", "DarkKhaki",
    "DarkMagenta", "DarkOliveGreen", "DarkOrange", "DarkOrchid", "DarkRed", "DarkSalmon",
    "DarkSeaGreen", "DarkSlateBlue", "DarkSlateGray", "DarkTurquoise", "DarkViolet",
    "DeepPink", "DeepSkyBlue", "DimGray", "DodgerBlue", "FireBrick", "FloralWhite",
    "ForestGreen", "Fuchsia", "Gainsboro", "GhostWhite", "Gold", "GoldenRod", "Gray",
    "Green", "GreenYellow", "HoneyDew", "HotPink", "IndianRed", "Indigo", "Ivory", "Khaki",
    "Lavender", "LavenderBlush", "LawnGreen", "LemonChiffon", "LightBlue", "LightCoral",
    "LightCyan", "LightGoldenRodYellow", "LightGray", "LightGreen", "LightPink",
    "LightSalmon", "LightSeaGreen", "LightSlateGray", "LightSteelBlue",
    "LightYellow", "Lime", "LimeGreen", "Linen", "Magenta", "Maroon", "MediumAquaMarine",
    "MediumBlue", "MediumOrchid", "MediumPurple", "MediumSeaGreen", "MediumSlateBlue",
    "MediumSpringGreen", "MediumTurquoise", "MediumVioletRed", "MidnightBlue", "MintCream",
    "Moccasin", "NavajoWhite", "Navy", "OldLace", "Olive", "OliveDrab",
    "Orange", "OrangeRed", "Orchid", "PaleGoldenRod", "PaleGreen", "PaleTurquoise",
    "PaleVioletRed", "PapayaWhip", "PeachPuff", "Peru", "Pink", "Plum", "PowderBlue",
    "Purple", "Red", "RosyBrown", "RoyalBlue", "SaddleBrown", "Salmon",
    "SandyBrown", "SeaGreen", "SeaShell", "Sienna", "Silver", "SkyBlue", "SlateBlue",
    "SlateGray", "Snow", "SpringGreen", "SteelBlue", "Tan", "Teal", "Thistle", "Tomato",
    "Turquoise", "Violet", "Wheat", "White", "WhiteSmoke", "Yellow", "YellowGreen"
]


def generate_cylinder(filename):
    dwg = svgwrite.Drawing(filename=filename, debug=True, size=(480, 270))
    color = random.choice(svg_safe).lower()
    random_height_start = random.randint(30, 100)
    random_height_end = random.randint(random_height_start, 270)
    random_radius = random.randint(25, 100)
    center_circles = random.randint(100, 270)

    cylinder_center_x = center_circles
    cylinder_center_y = (random_height_start + random_height_end) / 2

    rotation_angle = random.randint(0, 360)

    shapes = dwg.add(dwg.g(id='shapes', fill=color, transform=f'rotate({
                     rotation_angle}, {cylinder_center_x}, {cylinder_center_y})'))

    body = dwg.rect(insert=(center_circles - random_radius, random_height_start),
                    size=(random_radius * 2, random_height_end -
                          random_height_start),
                    stroke=pick_color(), stroke_width=3)
    body.fill(pick_color(),  opacity=0.5)
    shapes.add(body)

    top = svgwrite.shapes.Ellipse(center=(center_circles, random_height_start),
                                  r=(random_radius, 25), stroke=pick_color(), stroke_width=3)
    shapes.add(top)

    bottom = svgwrite.shapes.Ellipse(center=(center_circles, random_height_end),
                                     r=(random_radius, 25), stroke=pick_color(), stroke_width=3)
    shapes.add(bottom)

    dwg.save()


def pick_color():
    return random.choice(svg_safe).lower()


def pick_color_transparent():

    fill_color = pick_color()

    alpha = 0.5

    alpha_hex = int(alpha * 255)
    alpha_hex_str = format(alpha_hex, '02x')

    fill_color_with_opacity = f"{fill_color}{alpha_hex_str}"
    return fill_color_with_opacity


def generate_triangle(filename, width, height, min_shape_size, max_shape_size, fill_random=True):
    dwg = svgwrite.Drawing(filename, size=(
        "480px", "270px"), viewBox=('0 0 480 270'))
    triangle_size = random.uniform(min_shape_size, max_shape_size)
    max_triangle_x = width - triangle_size
    max_triangle_y = height - (triangle_size * math.sqrt(3) / 2)
    triangle_x = random.uniform(0, max_triangle_x)
    triangle_y = random.uniform(0, max_triangle_y)
    rotation_angle = random.uniform(0, 360)

    if fill_random:
        fill = random.choice(["none", pick_color()])
    else:
        fill = "none"
    points = [(triangle_x, triangle_y), (triangle_x + triangle_size, triangle_y),
              (triangle_x + triangle_size / 2, triangle_y + triangle_size * math.sqrt(3) / 2)]
    dwg.add(dwg.polygon(stroke_width='3', points=points, fill=fill, stroke=pick_color(
    ), transform=f'rotate({rotation_angle},{triangle_x},{triangle_y})'))
    dwg.save()


def generate_pyramid(filename, width, height, min_shape_size, max_shape_size, fill_random=True):
    dwg = svgwrite.Drawing(filename, size=(
        f"{width}px", f"{height}px"), viewBox=('0 0 480 270'))
    pyramid_x = random.uniform(-20, width - 20)
    pyramid_y = random.uniform(-20, height - 20)
    if fill_random:
        fill_color = pick_color()
    else:
        fill_color = "none"
    min_scale = min_shape_size / max(width, height)
    max_scale = max_shape_size / max(width, height)
    scale = random.uniform(min_scale, max_scale)

    paths = [
        "M 324,45 L 312,355 L 30,492",
        "M 633,418 L 312,355",
        "M 30,492 L 375,605 L 634,417 L 323,44 L 30,492 z",
        "M 324,45 L 375,605"
    ]

    for path in paths:
        transformed_path = dwg.path(
            d=path, stroke=pick_color(), stroke_width='3', fill=fill_color)
        transformed_path.scale(scale)
        transformed_path.translate(
            pyramid_x, pyramid_y)
        dwg.add(transformed_path)
    dwg.save()


def generate_sphere(filename, width, height, min_radius, max_radius, fill_random=True):
    dwg = svgwrite.Drawing(filename, size=(
        "480px", "270px"), viewBox=('0 0 480 270'))
    circle_radius = random.uniform(min_radius, max_radius)
    circle_center = (width / 2, height / 2)
    if fill_random:
        fill = random.choice(["none", pick_color()])
    else:
        fill = "none"
    dwg.add(dwg.circle(center=circle_center,
            r=circle_radius, fill=fill, stroke='black'))
    dwg.save()


def generate_cube(filename):
    size = random.randint(100, 600)
    cube_size = size / 2
    dwg = svgwrite.Drawing(filename, size=(
        "480px", "270px"), viewBox='0 0 480 270')

    vertices = [
        (-0.15 * cube_size, 0.15 * cube_size), (-0.05 * cube_size, 0.05 * cube_size),
        (0.05 * cube_size, 0.15 * cube_size), (0.15 * cube_size, 0.05 * cube_size),
        (-0.15 * cube_size, -0.05 * cube_size), (-0.05 * cube_size, -0.15 * cube_size),
        (0.05 * cube_size, -0.05 * cube_size), (0.15 * cube_size, -0.15 * cube_size)
    ]

    lines = [
        (0, 1), (2, 3), (4, 5), (6, 7),
        (0, 2), (1, 3), (4, 6), (5, 7),
        (0, 4), (1, 5), (2, 6), (3, 7)
    ]
    center_x = 240
    center_y = 135
    cube_x = random.uniform(cube_size, 480 - cube_size)
    cube_y = random.uniform(cube_size, 270 - cube_size)
    rotation_angle = random.randint(0, 360)
    rotated_vertices = [
        (
            center_x + (x * math.cos(math.radians(rotation_angle)) -
                        y * math.sin(math.radians(rotation_angle))),
            center_y + (x * math.sin(math.radians(rotation_angle)) +
                        y * math.cos(math.radians(rotation_angle)))
        ) for x, y in vertices
    ]

    color = pick_color()
    for start, end in lines:
        dwg.add(dwg.line(
            start=(rotated_vertices[start][0] + cube_x - center_x,
                   rotated_vertices[start][1] + cube_y - center_y),
            end=(rotated_vertices[end][0] + cube_x - center_x,
                 rotated_vertices[end][1] + cube_y - center_y),
            stroke=color))

    dwg.save()


def generate_square(filename, width, height, min_shape_size, max_shape_size, fill_random=True):
    dwg = svgwrite.Drawing(filename, size=(
        "480px", "270px"), viewBox=('0 0 480 270'))
    square_size = random.uniform(min_shape_size, max_shape_size)
    max_square_x = width - square_size
    max_square_y = height - square_size
    square_x = random.uniform(0, max_square_x)
    square_y = random.uniform(0, max_square_y)

    if fill_random:
        fill = pick_color()
    else:
        fill = "none"
    center_x = square_x + square_size / 2
    center_y = square_y + square_size / 2
    rotation_angle = random.uniform(0, 360)
    square = dwg.rect(insert=(square_x, square_y), size=(
        square_size, square_size), fill=fill, stroke=pick_color(), transform=f'rotate({rotation_angle},{center_x},{center_y})', stroke_width='5')
    dwg.add(square)
    dwg.save()


def generate_circle(filename):
    height = random.randint(100, 400)
    width = height
    dwg = svgwrite.Drawing(filename, size=(
        "480px", "270px"), viewBox=('0 0 480 270'))
    circle_radius = random.uniform(10, min(width, height) / 2)
    circle_x = random.uniform(circle_radius, width - circle_radius)
    circle_y = random.uniform(circle_radius, height - circle_radius)
    fill = pick_color()
    dwg.add(dwg.circle(center=(circle_x, circle_y), r=circle_radius, fill=fill))
    dwg.save()



shapes = [
    'cylinder',
    'square',
    'circle',
    'triangle',
    'cube',
    'sphere',
    'pyramid',
]


def generate_shape(i, shape):
    generate_type = 'train'
    width = 480
    height = 270
    min_shape_size = 50
    max_shape_size = 150
    match shape:
        case 'cylinder':
            return generate_cylinder(f'{generate_type}/cylinder/cylinder-{i}.svg')
        case 'square':
            return generate_square(
                    f'{generate_type}/square/square-{i}.svg', width, height, min_shape_size, max_shape_size)
        case 'circle':
            return generate_circle(f'{generate_type}/circle/circle-{i}.svg')
        case 'triangle':
            return generate_triangle(
                    f'{generate_type}/triangle/triangle-{i}.svg', width, height, min_shape_size, max_shape_size)
        case 'cube':
            return generate_cube(f'{generate_type}/cube/cube-{i}.svg')
        case 'sphere':
            return generate_sphere(
                    f'{generate_type}/sphere/sphere-{i}.svg', width, height, min_shape_size, max_shape_size)
        case 'pyramid':
            return generate_pyramid(
                    f'{generate_type}/pyramid/pyramid-{i}.svg', width, height, min_shape_size, max_shape_size)
        case _:
            return "Something's wrong with the internet"