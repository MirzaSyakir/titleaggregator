document.addEventListener("DOMContentLoaded", function() {
    const headlineContainer = document.getElementById("headline-container");

    // Fetch headlines from the JSON file
    fetch('headlines.json')
        .then(response => response.json())
        .then(data => {
            // Display headlines on the webpage
            data.forEach(article => {
                const headlineBox = document.createElement("div");
                headlineBox.classList.add("headline-box"); // Add the box class
                headlineBox.innerHTML = `<a href="${article.link}" target="_blank">${article.title}</a> - ${article.pub_date}`;
                headlineContainer.appendChild(headlineBox);
            });
        })
        .catch(error => console.error('Error fetching headlines:', error));
});
