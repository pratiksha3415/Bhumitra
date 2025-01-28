// Sample data for districts, talukas, villages, and tehsils
const districts = ['Agra', 'Lucknow', 'Kanpur', 'Varanasi', 'Prayagraj'];
const talukas = {
    'Agra': ['Etmadpur', 'Fatehabad', 'Kiraoli'],
    'Lucknow': ['Bakshi Ka Talab', 'Malihabad', 'Mohanlalganj'],
    'Kanpur': ['Bilhaur', 'Ghatampur', 'Bhitargaon'],
    'Varanasi': ['Pindra', 'Rajatalab', 'Sevapuri'],
    'Prayagraj': ['Soraon', 'Phulpur', 'Handia']
};

// Generate random land data
function generateLandData() {
    const owners = [];
    const plots = [];
    
    // Generate 50 unique owners
    for (let i = 1; i <= 50; i++) {
        owners.push(`Owner ${i}`);
    }
    
    // Generate 75 plots with some owners having multiple plots
    for (let i = 1; i <= 75; i++) {
        const randomOwner = owners[Math.floor(Math.random() * owners.length)];
        plots.push({
            ownerName: randomOwner,
            plotNumber: `PLT${String(i).padStart(3, '0')}`,
            area: (Math.random() * 10 + 1).toFixed(2),
            khataNumber: `KH${String(Math.floor(Math.random() * 1000)).padStart(3, '0')}`,
            latitude: (26 + Math.random()).toFixed(6),
            longitude: (80 + Math.random()).toFixed(6),
            landQuality: ['Excellent', 'Good', 'Average', 'Poor'][Math.floor(Math.random() * 4)],
            proximity: `${Math.floor(Math.random() * 10 + 1)}km to city center`,
            usagePatterns: ['Agricultural', 'Residential', 'Commercial', 'Mixed Use'][Math.floor(Math.random() * 4)],
            waterDrainage: ['Excellent', 'Good', 'Fair', 'Poor'][Math.floor(Math.random() * 4)]
        });
    }
    
    return plots;
}

// Populate dropdowns
function populateDropdown(selectId, options) {
    const select = document.getElementById(selectId);
    select.innerHTML = '<option value="">Select ' + selectId.replace('Select', '') + '</option>';
    options.forEach(option => {
        const opt = document.createElement('option');
        opt.value = option;
        opt.textContent = option;
        select.appendChild(opt);
    });
}

// Initialize the page
document.addEventListener('DOMContentLoaded', function() {
    // Populate districts dropdown
    populateDropdown('districtSelect', districts);
    
    // Add event listener for district selection
    document.getElementById('districtSelect').addEventListener('change', function(e) {
        const selectedDistrict = e.target.value;
        if (selectedDistrict && talukas[selectedDistrict]) {
            populateDropdown('talukaSelect', talukas[selectedDistrict]);
        }
    });
    
    // Generate and display land data
    const landData = generateLandData();
    const tableBody = document.getElementById('landDataBody');
    
    landData.forEach(plot => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${plot.ownerName}</td>
            <td>${plot.plotNumber}</td>
            <td>${plot.area}</td>
            <td>${plot.khataNumber}</td>
            <td>${plot.latitude}</td>
            <td>${plot.longitude}</td>
            <td>${plot.landQuality}</td>
            <td>${plot.proximity}</td>
            <td>${plot.usagePatterns}</td>
            <td>${plot.waterDrainage}</td>
        `;
        tableBody.appendChild(row);
    });
    
    // Add event listeners for map buttons
    document.querySelector('.view-map-btn').addEventListener('click', () => {
        alert('Map view functionality will be implemented here');
    });
    
    document.querySelector('.download-map-btn').addEventListener('click', () => {
        alert('Map download functionality will be implemented here');
    });
});

// Add search functionality to dropdowns
document.querySelectorAll('.custom-select').forEach(select => {
    select.addEventListener('keyup', function(e) {
        const searchText = e.target.value.toLowerCase();
        Array.from(select.options).forEach(option => {
            const optionText = option.textContent.toLowerCase();
            option.style.display = optionText.includes(searchText) ? '' : 'none';
        });
    });
});