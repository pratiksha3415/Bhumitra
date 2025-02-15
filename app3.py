from flask import Flask, render_template, request, jsonify, send_from_directory
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
PLOT_FOLDER = "static/plots"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PLOT_FOLDER, exist_ok=True)

def generate_voronoi_map(file_path):
    """Generate a Voronoi-based cadastral map from an Excel file."""
    plot_data = pd.read_excel(file_path)
    plot_data = plot_data[['Sr_No', 'Evaluated_Area']]
    
    num_plots = len(plot_data)
    np.random.seed(42)
    points = np.random.rand(num_plots, 2) * 100  

    vor = Voronoi(points)
    fig, ax = plt.subplots(figsize=(8, 8))
    
    voronoi_plot_2d(vor, ax=ax, show_vertices=False, line_colors='black', 
                    line_width=1.5, line_alpha=0.6, point_size=5)

    # Add labels
    for i, (x, y) in enumerate(points):
        plt.text(x, y, f"P{plot_data.iloc[i]['Sr_No']}", fontsize=10, ha='center', va='center',
                 bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.3'))

    # Dynamic axis adjustment
    x_min, y_min = np.min(points, axis=0) - 5
    x_max, y_max = np.max(points, axis=0) + 5
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)

    ax.set_xlabel("X Coordinate")
    ax.set_ylabel("Y Coordinate")
    ax.set_title("Randomized Cadastral Map using Voronoi Diagram")

    output_path = os.path.join(PLOT_FOLDER, "voronoi_map.png")
    plt.savefig(output_path)
    plt.close()
    
    return "static/plots/voronoi_map.png"


@app.route('/')
def home():
    return render_template('index5.html')
# Route for the second page
@app.route('/second_page')
def second_page():
    return render_template('index6.html')

@app.route("/upload", methods=["POST"])
def upload():
    """Handle file upload and generate Voronoi map."""
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)
    
    image_path = generate_voronoi_map(file_path)
    return jsonify({"image_url": image_path})

if __name__ == "__main__":
    app.run(debug=True)
