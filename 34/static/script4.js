let regionCounter = 1; // Track the region number

document.getElementById('uploadBtn').addEventListener('click', function() {
    const fileInput = document.getElementById('fileInput');
    if (fileInput.files.length === 0) {
        alert("Please select at least one file!");
        return;
    }

    const formData = new FormData();
    for (const file of fileInput.files) {
        formData.append("files", file);
    }

    fetch("/upload", { method: "POST", body: formData })
        .then(response => response.json())
        .then(data => {
            if (data.map_paths) {
                data.map_paths.forEach(displayMap);
            } else {
                alert("Processing failed!");
            }
        })
        .catch(error => console.error("Error:", error));
});

function displayMap(filePath) {
    const mapContainer = document.getElementById('map-container');

    // Create region title
    const regionTitle = document.createElement('h3');
    regionTitle.textContent = `Region ${regionCounter}`;
    regionTitle.style.marginTop = "20px";
    regionTitle.style.fontSize = "20px";
    regionTitle.style.fontWeight = "bold";

    // Create image element for the map
    const img = document.createElement('img');
    img.src = filePath;
    img.className = "map-box";
    img.style.width = "400px";  // Adjust size if needed
    img.style.height = "auto";
    img.style.border = "2px solid #333";
    img.style.borderRadius = "8px";
    img.style.boxShadow = "0px 4px 10px rgba(0,0,0,0.2)";

    // Append title and image
    mapContainer.appendChild(regionTitle);
    mapContainer.appendChild(img);

    regionCounter++; // Increment for next region
}
