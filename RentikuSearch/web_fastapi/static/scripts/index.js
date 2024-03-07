document.addEventListener('DOMContentLoaded', function () {
    const propertyGallery = document.getElementById('property-gallery');

    // Use the Fetch API to get property data (replace URL with your actual API endpoint)
    fetch('http://127.0.0.1:8000/api/v1/property')
        .then(response => response.json())
        .then(data => {
            // Loop through the property data and create HTML for each item
            data.forEach(property => {
                const propertyItem = document.createElement('div');
                propertyItem.className = 'property-item';

                const propertyImage = document.createElement('img');
                propertyImage.src =  "image-src";//property.imageUrl;
                propertyImage.alt = property.title;

                const propertyTitle = document.createElement('h3');
                propertyTitle.textContent = property.title;

                const propertyPrice = document.createElement('p');
                propertyPrice.textContent = `$${property.price}`;

                // Append elements to the property item
                propertyItem.appendChild(propertyImage);
                propertyItem.appendChild(propertyTitle);
                propertyItem.appendChild(propertyPrice);

                // Append the property item to the gallery
                propertyGallery.appendChild(propertyItem);
            });
        })
        .catch(error => console.error('Error fetching property data:', error));
});

