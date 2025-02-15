from flask import Flask, render_template, request, send_from_directory, jsonify
import os
import matplotlib.pyplot as plt
from Shapelesspython import read_shapes_from_excel, plot_shape

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
MAP_FOLDER = 'static/maps'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAP_FOLDER'] = MAP_FOLDER

# Ensure directories exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(MAP_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return render_template('index3.html')

# Route for the second page
@app.route('/second_page')
def second_page():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'files' not in request.files:
        return jsonify({"error": "No files part"})

    files = request.files.getlist('files')
    map_paths = []

    for file in files:
        if file.filename == '':
            continue

        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

        # Process and generate a map for each file
        output_map = process_cadastral_data(file_path, file.filename)
        map_paths.append(f"/maps/{output_map}")

    return jsonify({"message": "Files processed", "map_paths": map_paths})

@app.route('/maps/<filename>')
def get_map(filename):
    return send_from_directory(app.config['MAP_FOLDER'], filename)

def process_cadastral_data(file_path, filename):
    """Processes cadastral data and generates a map image."""
    shapes, all_x, all_y = read_shapes_from_excel(file_path)

    plt.figure(figsize=(6,6))
    for shape, name, color in shapes:
        plot_shape(shape, name=name, color=color)

    plt.xlim(min(all_x) - 2, max(all_x) + 2)
    plt.ylim(min(all_y) - 2, max(all_y) + 2)
    plt.gca().set_aspect('equal')
    plt.grid(False)

    output_file = filename.replace('.xlsx', '.png')
    output_path = os.path.join(app.config['MAP_FOLDER'], output_file)
    plt.savefig(output_path)
    plt.close()

    return output_file

if __name__ == '__main__':
    app.run(debug=True)
