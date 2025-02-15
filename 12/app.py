import os
import cv2
import numpy as np
from flask import Flask, request, render_template, send_from_directory, redirect, url_for, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from PIL import Image
import torch
import torchvision.transforms as T
from flask import Flask, request, jsonify
import io
from sklearn.cluster import KMeans


app = Flask(__name__)
CORS(app)

# Configure upload and processed folders
UPLOAD_FOLDER = "static/uploads"
PROCESSED_FOLDER = "static/processed"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["PROCESSED_FOLDER"] = PROCESSED_FOLDER

# Ensure required directories exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)


# Image processing functions
def colored_edge_detection(image_path, output_path):
    """Process the image and save the processed version."""
    image = cv2.imread(image_path)

    if image is None:
        print(f"Error: Could not load image at '{image_path}'. Check the file path.")
        return None

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply CLAHE (Adaptive Histogram Equalization)
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    enhanced = clahe.apply(gray)

    # Apply Bilateral Filter to reduce noise while preserving edges
    filtered = cv2.bilateralFilter(enhanced, d=9, sigmaColor=75, sigmaSpace=75)

    # Apply Canny edge detection
    edges = cv2.Canny(filtered, 50, 150)

    # Use Morphological Closing to connect broken edges
    kernel = np.ones((5, 5), np.uint8)
    closed_edges = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)

    # Convert edges to neon yellow overlay
    neon_yellow_edges = np.zeros_like(image, dtype=np.uint8)
    neon_yellow_edges[:, :, 1] = closed_edges  # Green channel
    neon_yellow_edges[:, :, 2] = closed_edges  # Red channel

    # Blend original image with neon yellow overlay
    highlighted_edges = cv2.addWeighted(image, 0.8, neon_yellow_edges, 0.5, 0)

    # Extract polygon boundaries
    final_output = extract_black_polygon_from_image(highlighted_edges, closed_edges)

    # Save processed image
    cv2.imwrite(output_path, final_output)
    
    return os.path.basename(output_path)

def extract_black_polygon_from_image(image, edge_map):
    """Extracts and highlights polygon boundaries from the edge map."""
    contours, _ = cv2.findContours(edge_map, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Create a white background
    polygon_image = np.ones_like(image) * 255  # White background

    # Draw all detected boundaries as closed polygons
    cv2.drawContours(polygon_image, contours, -1, (0, 0, 0), 2)  # Black boundary

    return polygon_image
'''
@app.route("/", methods=["GET", "POST"])
def upload_and_process():
    """Handles file upload, processing, and redirects to the result page."""
    if request.method == "POST":
        print("Processing POST request...")  # Debugging
        if "file" not in request.files:
            print("No file part found.")  # Debugging
            return "No file part"

        file = request.files["file"]
        if file.filename == "":
            print("No selected file.")  # Debugging
            return "No selected file"

        if file:
            file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            processed_path = os.path.join(app.config["PROCESSED_FOLDER"], file.filename)

            print(f"Saving file to: {file_path}")  # Debugging
            file.save(file_path)  # Save uploaded file
            
            processed_image = colored_edge_detection(file_path, processed_path)  # Process image
            
            if processed_image:
                print(f"Processed image saved to: {processed_path}")  # Debugging
                return redirect(url_for("result_page", image=processed_image))  # Redirect to result page
            else:
                print("Image processing failed.")  # Debugging
                return "Image processing failed."

    return render_template("index2.html")'''
# Define Segmentation Colors
CLASS_COLORS = {
    0: (0, 0, 0),  # Background - Black
    21: (34, 139, 34),  # Forest - Green
    7: (255, 255, 0),  # Infrastructure - Yellow
    24: (0, 191, 255)  # River - Blue
}

# Preprocess Image
def preprocess_image(image):
    transform = T.Compose([
        T.Resize((512, 512)),
        T.ToTensor(),
        T.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    return transform(image).unsqueeze(0)

# Run Segmentation
def segment_image(image_tensor):
    with torch.no_grad():
        output = model(image_tensor)['out'][0]
    return output.argmax(0).byte().cpu().numpy()

# Apply Color Mask
def apply_color_mask(mask):
    h, w = mask.shape
    color_mask = np.zeros((h, w, 3), dtype=np.uint8)
    for class_id, color in CLASS_COLORS.items():
        color_mask[mask == class_id] = color
    return color_mask


# Define custom color map for land classification
COLOR_MAP = [
    [139, 69, 19],   # Brown (land)
    [34, 139, 34],   # Green (forest)
    [0, 0, 255]      # Blue (water)
]

# Soil Analysis Function using k-means clustering

def soil_analysis(image_path, output_path, k=3):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert to RGB
    
    # Reshape the image to a 2D array of pixels
    pixel_values = image.reshape((-1, 3))
    pixel_values = np.float32(pixel_values)
    
    # Apply k-means clustering with increased accuracy
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 200, 0.1)
    _, labels, centers = cv2.kmeans(pixel_values, k, None, criteria, 20, cv2.KMEANS_RANDOM_CENTERS)
    
    # Convert centers to integer values
    centers = np.uint8(centers)
    
    # Map labels to center colors
    segmented_image = centers[labels.flatten()]
    segmented_image = segmented_image.reshape(image.shape)
    
    # Apply color coding for land classification
    gray = cv2.cvtColor(segmented_image, cv2.COLOR_RGB2GRAY)
    unique_vals = np.unique(gray)
    output_image = np.zeros_like(segmented_image)
    
    for i, val in enumerate(unique_vals[:len(COLOR_MAP)]):  # Assign colors based on unique values
        mask = gray == val
        output_image[mask] = COLOR_MAP[i]
    
    cv2.imwrite(output_path, output_image)
    
def classify_land_types(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    result = np.zeros_like(image)
    
    # Define color ranges for different land types
    vegetation_mask = cv2.inRange(hsv, (35, 25, 25), (85, 255, 255))
    water_mask = cv2.inRange(hsv, (90, 50, 50), (130, 255, 255))
    urban_mask = cv2.inRange(hsv, (0, 0, 50), (180, 50, 200))
    
    # Apply colors
    result[vegetation_mask > 0] = [34, 139, 34]  # Green for vegetation
    result[water_mask > 0] = [255, 0, 0]         # Blue for water
    result[urban_mask > 0] = [128, 128, 128]     # Gray for urban
    
    return result



def process_infrastructure(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (256, 256))

    # Create segmentation mask
    segmentation_mask = np.zeros((image.shape[0], image.shape[1]))
    
    # Assign classes based on color intensities
    segmentation_mask[image[:, :, 0] > 150] = 1  # Infrastructure (Yellow)
    segmentation_mask[image[:, :, 1] > 150] = 2  # Vegetation (Green)
    segmentation_mask[image[:, :, 2] > 150] = 3  # Water Bodies (Blue)

    # Define colors for different classes
    class_colors = {
        0: [0, 0, 0],       # Background (Black)
        1: [255, 255, 0],   # Infrastructure (Yellow)
        2: [0, 255, 0],     # Vegetation (Green)
        3: [0, 255, 255],   # Water Bodies (Cyan)
    }

    # Create colored mask
    colored_mask = np.zeros((image.shape[0], image.shape[1], 3), dtype=np.uint8)
    for class_id, color in class_colors.items():
        colored_mask[segmentation_mask == class_id] = color

    return colored_mask

def water_analysis(image_path, output_path, k=3):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert to RGB
    
    # Reshape the image to a 2D array of pixels
    pixel_values = image.reshape((-1, 3))
    pixel_values = np.float32(pixel_values)
    
    # Apply k-means clustering with increased accuracy
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 200, 0.1)
    _, labels, centers = cv2.kmeans(pixel_values, k, None, criteria, 20, cv2.KMEANS_RANDOM_CENTERS)
    
    # Convert centers to integer values
    centers = np.uint8(centers)
    
    # Map labels to center colors
    segmented_image = centers[labels.flatten()]
    segmented_image = segmented_image.reshape(image.shape)
    
    # Apply color coding for land classification
    gray = cv2.cvtColor(segmented_image, cv2.COLOR_RGB2GRAY)
    unique_vals = np.unique(gray)
    output_image = np.zeros_like(segmented_image)
    
    for i, val in enumerate(unique_vals[:len(COLOR_MAP)]):  # Assign colors based on unique values
        mask = gray == val
        output_image[mask] = COLOR_MAP[i]
    
    cv2.imwrite(output_path, output_image)


@app.route('/')
def home():
    return render_template('index1.html')
# Route for the second page
@app.route('/second_page')
def second_page():
    return render_template('index2.html')
    


@app.route("/edge-detection", methods=["POST"])
def process_edge_detection():
    if "file" not in request.files:
        return "No file part", 400
    
    file = request.files["file"]
    if file.filename == "":
        return "No selected file", 400

    if file:
        file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        processed_path = os.path.join(app.config["PROCESSED_FOLDER"], f"edge_{file.filename}")
        file.save(file_path)
        
        colored_edge_detection(file_path, processed_path)
        return redirect(url_for("result_page", image=f"edge_{file.filename}"))

@app.route("/analyze-soil", methods=["POST"])
def process_soil():
    if "file" not in request.files:
        return "No file part", 400
    
    file = request.files["file"]
    if file.filename == "":
        return "No selected file", 400

    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        processed_path = os.path.join(app.config["PROCESSED_FOLDER"], f"soil_{file.filename}")
        file.save(file_path)
        
        soil_analysis(file_path, processed_path)
        return redirect(url_for("result_page", image=f"soil_{file.filename}"))

@app.route("/forest-analysis", methods=["POST"])
def process_forest():
    if "file" not in request.files:
        return "No file part", 400
    
    file = request.files["file"]
    if file.filename == "":
        return "No selected file", 400

    if file:
        file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        processed_path = os.path.join(app.config["PROCESSED_FOLDER"], f"forest_{file.filename}")
        file.save(file_path)
        
        image = cv2.imread(file_path)
        classified_image = classify_land_types(image)
        cv2.imwrite(processed_path, classified_image)
        return redirect(url_for("result_page", image=f"forest_{file.filename}"))

@app.route("/infrastructure-analysis", methods=["POST"])
def process_infra():
    if "file" not in request.files:
        return "No file part", 400
    
    file = request.files["file"]
    if file.filename == "":
        return "No selected file", 400

    if file:
        file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        processed_path = os.path.join(app.config["PROCESSED_FOLDER"], f"infra_{file.filename}")
        file.save(file_path)
        
        image = cv2.imread(file_path)
        if image is None:
            return "Error reading image", 500  # Handle invalid image error
        
        result = process_infrastructure(image)  # Pass the image array, not path
        cv2.imwrite(processed_path, result)
        
        return redirect(url_for("result_page", image=f"infra_{file.filename}"))


@app.route("/water-analysis", methods=["POST"])
def process_water():
    """Processes uploaded image and returns a segmented version."""
    file = request.files.get("file")

    if not file or file.filename == "":
        return jsonify({"error": "No valid file uploaded"}), 400

    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    processed_path = os.path.join(app.config["PROCESSED_FOLDER"], f"water_{filename}")

    # Ensure directories exist
    os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)
    os.makedirs(app.config["PROCESSED_FOLDER"], exist_ok=True)

    file.save(file_path)

    try:
        # Define colors: Brown (land), Green (forest), Blue (water)
        global COLOR_MAP
        COLOR_MAP = [
            [139, 69, 19],   # Brown (land)
            [34, 139, 34],   # Green (forest)
            [0, 0, 255]      # Blue (water)
        ]

        # Process image using the updated segmentation function
        water_analysis(file_path, processed_path, k=3)

        # Redirect to result page with the processed image filename
        return redirect(url_for("result_page", image=f"water_{filename}"))
    
    except Exception as e:
        return jsonify({"error": f"Processing failed: {str(e)}"}), 500


@app.route("/result")
def result_page():
    image = request.args.get("image", "")
    if not image:
        return "No image found.", 400
    
    image_url = f"/static/processed/{image}"
    return render_template("index2.html", image_url=image_url)

@app.route("/static/processed/<filename>")
def serve_processed(filename):
    return send_from_directory(app.config["PROCESSED_FOLDER"], filename)

if __name__ == "__main__":
    app.run(debug=True)