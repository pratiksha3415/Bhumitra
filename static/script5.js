document.addEventListener("DOMContentLoaded", function () {
    let data = [
        {"Sr_No":1,"Owner_Name":"Amit Desai","Total_Area":59,"Avg":3.69,"Percentage_Result":73.75,"Evaluated_Area":43},
        {"Sr_No":2,"Owner_Name":"Anjali Choudhary","Total_Area":57,"Avg":3.79,"Percentage_Result":75.83,"Evaluated_Area":42},
        {"Sr_No":3,"Owner_Name":"Arjun Patel","Total_Area":52,"Avg":3.31,"Percentage_Result":66.25,"Evaluated_Area":34},
        {"Sr_No":4,"Owner_Name":"Deepak Malhotra","Total_Area":65,"Avg":3.75,"Percentage_Result":75.0,"Evaluated_Area":48},
        {"Sr_No":5,"Owner_Name":"Kavita Nair","Total_Area":61,"Avg":3.66,"Percentage_Result":73.13,"Evaluated_Area":44},
        {"Sr_No":6,"Owner_Name":"Manish Gupta","Total_Area":60,"Avg":3.34,"Percentage_Result":66.88,"Evaluated_Area":39},
        {"Sr_No":7,"Owner_Name":"Meena Iyer","Total_Area":61,"Avg":3.63,"Percentage_Result":72.5,"Evaluated_Area":44},
        {"Sr_No":8,"Owner_Name":"Neha Bansal","Total_Area":64,"Avg":3.63,"Percentage_Result":72.5,"Evaluated_Area":46},
        {"Sr_No":9,"Owner_Name":"Poonam Agarwal","Total_Area":51,"Avg":3.44,"Percentage_Result":68.75,"Evaluated_Area":34},
        {"Sr_No":10,"Owner_Name":"Priya Verma","Total_Area":63,"Avg":3.71,"Percentage_Result":74.17,"Evaluated_Area":46},
        {"Sr_No":11,"Owner_Name":"Rajesh Sharma","Total_Area":48,"Avg":3.31,"Percentage_Result":66.25,"Evaluated_Area":31},
        {"Sr_No":12,"Owner_Name":"Ritesh Bakare","Total_Area":24,"Avg":3.25,"Percentage_Result":65.0,"Evaluated_Area":15},
        {"Sr_No":13,"Owner_Name":"Rohit Mehta","Total_Area":44,"Avg":3.38,"Percentage_Result":67.5,"Evaluated_Area":29},
        {"Sr_No":14,"Owner_Name":"Sneha Kulkarni","Total_Area":40,"Avg":3.83,"Percentage_Result":76.67,"Evaluated_Area":30},
        {"Sr_No":15,"Owner_Name":"Sunita Joshi","Total_Area":47,"Avg":3.42,"Percentage_Result":68.33,"Evaluated_Area":32},
        {"Sr_No":16,"Owner_Name":"Suresh Reddy","Total_Area":25,"Avg":3.38,"Percentage_Result":67.5,"Evaluated_Area":16},
        {"Sr_No":17,"Owner_Name":"Vikram Singh","Total_Area":101,"Avg":3.56,"Percentage_Result":71.25,"Evaluated_Area":71}
    ];

    let tableBody = document.getElementById("tableBody");

    data.forEach(row => {
        let tr = document.createElement("tr");

        tr.innerHTML = `
            <td>${row.Sr_No}</td>
            <td>${row.Owner_Name}</td>
            <td>${row.Total_Area}</td>
            <td>${row.Evaluated_Area}</td>
            <td>${row.Avg}</td>
            <td>${row.Percentage_Result}</td>
        `;

        tableBody.appendChild(tr);
    });
});
