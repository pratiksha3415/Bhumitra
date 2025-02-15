Project Title :
	Land Consolidation (Chakbandi) using AI Algorithms

Project Description
This project aims to modernize Land Consolidation (Chakbandi) by utilizing AI algorithms and satellite imagery to streamline the process of land reorganization. The system automates land evaluation and consolidation by analyzing geographical and cadastral data, ensuring efficient and dispute-free land distribution.

Our web-based platform provides multiple AI-driven algorithms that:

Analyze satellite images to detect edges, boundaries, forests, water resources, and infrastructure.
Generate cadastral maps from the given geospatial data.
Evaluate land data based on Chakbandi requirements.
Display the final evaluated cadastral map for optimized land consolidation.
By integrating AI and geospatial analysis, this system ensures precision, fairness, and efficiency in land consolidation, benefiting farmers, landowners, and policymakers.

Our project utilizes a combination of frontend, backend, and data processing technologies to ensure efficient land consolidation using AI algorithms.

Frontend:

HTML, CSS, JavaScript, Bootstrap – For building an interactive and user-friendly web interface.
Backend:

Python (Flask) – For handling requests, processing data, and managing backend operations.
Data Processing & Analysis:

Pandas, NumPy – For handling and analyzing geospatial and cadastral data.
Matplotlib – For visualizing land maps and data insights.
Scipy (Voronoi, voronoi_plot_2d) – For generating and plotting Voronoi diagrams to assist in land segmentation.
Matplotlib Patches (Polygon) – For rendering land boundaries and infrastructure details.
Data Handling:

JSON – For structuring and exchanging data between the frontend and backend.
OS – For file management and handling system operations.
This robust tech stack enables precise data processing, AI-driven insights, and seamless user interaction for land consolidation.



### **Installation & Setup**  

Follow the steps below to set up and run the **Land Consolidation (Chakbandi) using AI Algorithms** project on your local machine.  

---

### **1. Prerequisites**  
Ensure you have the following installed on your system:  
- **Python (3.x)** – [Download & Install Python](https://www.python.org/downloads/)  
- **pip** (Python package manager) – Comes with Python by default  
- **Git** (optional, for cloning the repository) – [Download & Install Git](https://git-scm.com/downloads)  

---

### **2. Clone the Repository**  
Use Git to clone the project repository:  
```bash
git clone <repository_url>
cd <project_directory>
```
If you don’t have Git, you can download the repository as a ZIP file and extract it manually.  

---

### **3. Set Up a Virtual Environment** (Recommended)  
Creating a virtual environment helps manage dependencies efficiently.  

```bash
python -m venv venv   # Create a virtual environment
source venv/bin/activate   # Activate on macOS/Linux
venv\Scripts\activate      # Activate on Windows
```

---

### **4. Install Required Dependencies**  
Install all necessary Python libraries using:  

```bash
pip install flask pandas numpy matplotlib scipy
```

---

### **5. Run the Flask Server**  
Execute the following command to start the backend server:  
```bash
python app.py
```
By default, the Flask server will run on:  
📌 `http://127.0.0.1:5000/`  

---

### **6. Open the Web Application**  
- Open your browser and go to:  
  **`http://127.0.0.1:5000/`**  
- You should see the web interface for **Land Consolidation (Chakbandi) using AI Algorithms**.  

---

### **7. How to Use the System**  
1. **Upload a Satellite Image**  
   - The system processes the image using AI algorithms.  
2. **AI-based Detection & Analysis**  
   - Detects **edges, boundaries, forests, water resources, and infrastructure** from the satellite image.  
3. **Cadastral Map Generation**  
   - Generates a cadastral map based on the given data.  
4. **Land Consolidation Evaluation**  
   - Processes the data and provides a **final evaluated Chakbandi cadastral map**.  
5. **View Results**  
   - The system displays the optimized land consolidation map.  

---

### **8. Additional Commands**  
#### **To deactivate the virtual environment**  
```bash
deactivate
```
#### **To update dependencies**  
```bash
pip install --upgrade flask pandas numpy matplotlib scipy
```
#### **To check installed dependencies**  
```bash
pip freeze
```

### **Usage Guide**  

1. **Upload a Satellite Image**  
   - Users can upload satellite images to be processed.  

2. **AI-based Detection & Analysis**  
   - The system applies multiple AI algorithms to detect:  
     - Land **edges & boundaries**  
     - **Forests, water resources, and infrastructure**  

3. **Cadastral Map Generation**  
   - Converts processed data into a **cadastral map**.  

4. **Land Consolidation Evaluation**  
   - Analyzes land ownership and regulatory requirements.  
   - Suggests optimized **land redistribution plans**.  

5. **View & Download Final Map**  
   - Displays the final **evaluated Chakbandi cadastral map**.  
   - Users can download the generated map for reference.  

---

### **System Architecture**  

The project follows a **modular architecture** combining **frontend, backend, and AI-based processing**.  

1. **Frontend (Client-side)**  
   - Developed using **HTML, CSS, JavaScript, and Bootstrap**.  
   - Handles **user input** and **displays results**.  

2. **Backend (Server-side)**  
   - Built with **Flask (Python)** for handling requests.  
   - Processes **uploaded satellite images**.  
   - Runs **AI-based detection algorithms**.  

3. **AI & Data Processing Module**  
   - Uses **Pandas, NumPy, Matplotlib, and SciPy**.  
   - **Detects land features** and **evaluates cadastral maps**.  
   - Implements **Voronoi diagrams** for land segmentation.  

4. **Database & File Handling**  
   - Uses **JSON & Pandas** for managing and structuring land data.  
   - Handles **user uploads** and **processed cadastral maps**.  

5. **Final Output**  
   - Generates an **optimized Chakbandi cadastral map**.  
   - Displays **evaluated results** for land consolidation.  

---

### **Contributing**  

We welcome contributions to improve this project!  

#### **How to Contribute**  
1. **Fork the Repository**  
   - Click the **Fork** button on GitHub.  

2. **Clone the Project**  
   ```bash
   git clone <your-forked-repo-url>
   cd <project-directory>
   ```

3. **Create a Feature Branch**  
   ```bash
   git checkout -b feature-branch-name
   ```

4. **Make Changes & Commit**  
   - Implement your feature/fix.  
   - Commit changes:  
     ```bash
     git commit -m "Added new feature"
     ```

5. **Push to GitHub & Create a Pull Request**  
   ```bash
   git push origin feature-branch-name
   ```
   - Open a **Pull Request (PR)** in the original repository.  
   - Describe your changes and submit for review.  

#### **Contribution Guidelines**  
- Ensure **clean and well-documented code**.  
- Follow **best coding practices**.  
- Test all changes before submitting a **Pull Request**.  

---

### **License**  

This project is licensed under the **MIT License**.  

📜 **MIT License** grants permission to use, copy, modify, and distribute the software freely while requiring attribution to the original authors.  

---



