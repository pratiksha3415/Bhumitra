import matplotlib.pyplot as plt
import pandas as pd
import random

def generate_random_color():
    """Generates a random color."""
    return "#" + "".join(random.choices('0123456789ABCDEF', k=6))

def plot_shape(coordinates, name='', color=None):
    """Plots a cadastral shape."""
    if color is None:
        color = generate_random_color()
    
    x_values, y_values = zip(*coordinates)
    x_values += (x_values[0],)
    y_values += (y_values[0],)
    
    plt.fill(x_values, y_values, color=color, alpha=0.5)
    plt.plot(x_values, y_values, color=color, marker='o')

    centroid_x = sum(x_values) / len(x_values)
    centroid_y = sum(y_values) / len(y_values)
    plt.text(centroid_x, centroid_y, name, fontsize=12, ha='center', va='center', 
             bbox=dict(facecolor='white', alpha=0.6, edgecolor='black'))

def read_shapes_from_excel(file_path):
    """Reads cadastral shapes from an Excel file."""
    df = pd.read_excel(file_path)
    shapes = []
    all_x, all_y = [], []

    for _, row in df.iterrows():
        name = row['Name']
        coordinates = [tuple(map(int, coord.strip('()').split(','))) for coord in row['Coordinates'].split(';')]
        all_x.extend([x for x, y in coordinates])
        all_y.extend([y for x, y in coordinates])
        shapes.append((coordinates, name, None))
    
    return shapes, all_x, all_y
