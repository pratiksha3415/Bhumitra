// Dropdown data management
const dropdowns = {
    district: document.getElementById('district'),
    taluka: document.getElementById('taluka'),
    village: document.getElementById('village'),
    tehsil: document.getElementById('tehsil')
};

// Event listeners for dropdowns
dropdowns.district.addEventListener('change', function() {
    // Clear dependent dropdowns
    clearDropdowns(['taluka', 'village', 'tehsil']);
    
    if (this.value) {
        // Simulate loading data based on selection
        populateDependentDropdown('taluka', this.value);
    }
});

dropdowns.taluka.addEventListener('change', function() {
    clearDropdowns(['village', 'tehsil']);
    
    if (this.value) {
        populateDependentDropdown('village', this.value);
    }
});

dropdowns.village.addEventListener('change', function() {
    clearDropdowns(['tehsil']);
    
    if (this.value) {
        populateDependentDropdown('tehsil', this.value);
    }
});

// Helper functions
function clearDropdowns(dropdownIds) {
    dropdownIds.forEach(id => {
        dropdowns[id].innerHTML = `<option value="">Select ${id.charAt(0).toUpperCase() + id.slice(1)}</option>`;
        dropdowns[id].disabled = true;
    });
}

function populateDependentDropdown(dropdownId, parentValue) {
    // Enable the dropdown
    dropdowns[dropdownId].disabled = false;
    
    // Simulate loading data
    setTimeout(() => {
        // This is a placeholder. Replace with actual data when available
        const dummyOptions = ['Option 1', 'Option 2', 'Option 3'].map(option => 
            `<option value="${option.toLowerCase().replace(' ', '_')}">${option}</option>`
        ).join('');
        
        dropdowns[dropdownId].innerHTML = 
            `<option value="">Select ${dropdownId.charAt(0).toUpperCase() + dropdownId.slice(1)}</option>` + 
            dummyOptions;
    }, 500);
}

// Process button functionality
const processBtn = document.querySelector('.process-btn');
let isProcessing = false;

processBtn.addEventListener('click', function() {
    if (isProcessing) return;
    
    isProcessing = true;
    this.classList.add('processing');
    
    // Simulate processing
    setTimeout(() => {
        isProcessing = false;
        this.classList.remove('processing');
        // Add your data processing logic here
    }, 2000);
});

// Table data management
function populateTable(tableId, data) {
    const table = document.getElementById(tableId);
    const tbody = table.querySelector('tbody');
    
    // Clear existing rows
    tbody.innerHTML = '';
    
    // Add new rows
    data.forEach(row => {
        const tr = document.createElement('tr');
        Object.values(row).forEach(value => {
            const td = document.createElement('td');
            td.textContent = value;
            tr.appendChild(td);
        });
        tbody.appendChild(tr);
    });
}

// Initialize the page
document.addEventListener('DOMContentLoaded', function() {
    // Enable only the district dropdown initially
    Object.keys(dropdowns).forEach(id => {
        if (id !== 'district') {
            dropdowns[id].disabled = true;
        }
    });
});
document.addEventListener("DOMContentLoaded", function () {
    // Data extracted from Excel sheets
    const excelData = {
        "Region 1": [
            { Name: "P001", Coordinates: "(1,1);(3,1);(4,3);(2,3)" },
            { Name: "P002", Coordinates: "(4,3);(7,3);(8,6);(4,6)" },
            { Name: "P003", Coordinates: "(2,3);(4,3);(4,6);(1,7)" },
            { Name: "P004", Coordinates: "(6,9);(8,11);(7,14);(3,12)" },
            { Name: "P005", Coordinates: "(3,1);(7,3);(4,3)" }
        ],
        "Region 2": [
            { Name: "P001", Coordinates: "(1,15);(4,14);(7,17);(3,19)" },
            { Name: "P002", Coordinates: "(1,10);(5,11);(6,15);(4,14);(1,15)" },
            { Name: "P003", Coordinates: "(5,6);(10,9);(5,11);(1,10)" },
            { Name: "P004", Coordinates: "(3,2);(7,1);(9,5);(5,6)" },
            { Name: "P005", Coordinates: "(5,11);(10,9);(9,13);(6,15)" }
        ],
        "Region 3": [
            { Name: "P001", Coordinates: "(2,2);(7,2);(10,7);(5,5)" },
            { Name: "P002", Coordinates: "(5,5);(10,7);(9,10);(5,11);(2,9)" },
            { Name: "P003", Coordinates: "(2,9);(5,11);(8,16);(2,14)" },
            { Name: "P004", Coordinates: "(7,2);(12,2);(14,10);(10,7)" },
            { Name: "P005", Coordinates: "(10,7);(14,10);(12,12);(9,10)" }
        ],
        "Region 4": [
            { Name: "P001", Coordinates: "(10,3);(9,5);(11,7);(13,4)" },
            { Name: "P002", Coordinates: "(6,3);(5,6);(9,5);(10,3)" },
            { Name: "P003", Coordinates: "(3,2);(5,6);(6,3)" },
            { Name: "P004", Coordinates: "(3,2);(3,6);(5,6)" },
            { Name: "P005", Coordinates: "(3,6);(6,11);(5,6)" }
        ]
    };

    // Get the container to append tables
    const container = document.querySelector(".tables-container");

    // Function to create tables dynamically
    Object.keys(excelData).forEach((region, index) => {
        const tableWrapper = document.createElement("div");
        tableWrapper.classList.add("table-wrapper");

        const title = document.createElement("h2");
        title.textContent = region;
        tableWrapper.appendChild(title);

        const tableScroll = document.createElement("div");
        tableScroll.classList.add("table-scroll");

        const table = document.createElement("table");
        table.id = `table${index + 1}`;

        // Create table header
        const thead = document.createElement("thead");
        const headerRow = document.createElement("tr");
        ["Name", "Coordinates"].forEach((header) => {
            const th = document.createElement("th");
            th.textContent = header;
            headerRow.appendChild(th);
        });
        thead.appendChild(headerRow);
        table.appendChild(thead);

        // Create table body
        const tbody = document.createElement("tbody");
        excelData[region].forEach((row) => {
            const tr = document.createElement("tr");
            Object.values(row).forEach((value) => {
                const td = document.createElement("td");
                td.textContent = value;
                tr.appendChild(td);
            });
            tbody.appendChild(tr);
        });
        table.appendChild(tbody);

        tableScroll.appendChild(table);
        tableWrapper.appendChild(tableScroll);
        container.appendChild(tableWrapper);
    });
});
