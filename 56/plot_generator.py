import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi
from matplotlib.patches import Polygon

def generate_cadastral_map(file_path):
    # Step 1: Load Excel file
    plot_data = pd.read_excel(file_path)
    plot_data = plot_data[['Sr_No', 'Evaluated_Area']]

    # Step 2: Generate random coordinates for plots
    num_plots = len(plot_data)
    np.random.seed(42)  # For consistency
    points = np.random.rand(num_plots, 2) * 100  

    # Step 3: Generate Voronoi diagram
    vor = Voronoi(points)

    # Step 4: Generate random colors
    colors = np.random.rand(len(vor.regions), 3)

    # Step 5: Plot Voronoi diagram
    fig, ax = plt.subplots(figsize=(8, 8))

    for region_idx, region in enumerate(vor.regions):
        if not -1 in region and len(region) > 0:  # Exclude open regions
            polygon = [vor.vertices[i] for i in region]
            ax.add_patch(Polygon(polygon, color=colors[region_idx], alpha=0.5, edgecolor='black'))

    ax.scatter(points[:, 0], points[:, 1], color='black', marker='o', s=10, zorder=2)

    for i, (x, y) in enumerate(points):
        plt.text(x, y, f"P{plot_data.iloc[i]['Sr_No']}", fontsize=10, ha='center', va='center',
                 bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.3'))

    x_min, y_min = np.min(points, axis=0) - 5
    x_max, y_max = np.max(points, axis=0) + 5
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)

    ax.set_xlabel("X Coordinate")
    ax.set_ylabel("Y Coordinate")
    ax.set_title("Randomized Cadastral Map")

    output_path = "static/cadastral_map.png"
    plt.savefig(output_path)
    plt.close()
    
    return output_path
