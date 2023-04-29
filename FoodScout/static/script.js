document.getElementById("search-form").addEventListener("submit", function(event) {
  event.preventDefault();

  let restaurantType = document.getElementById("restaurant-type").value;
  let zipCode = document.getElementById("zip-code").value;

  let data = {
    restaurant_type: restaurantType,
    zip_code: zipCode
  };

  fetch('/search', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  })
  .then(response => response.json())
  .then(restaurants => {
    displayResults(restaurants);
  });
});

function displayResults(restaurants) {
  let resultsElement = document.getElementById("results");
  resultsElement.innerHTML = "";

  for (let restaurant of restaurants) {
    let listItem = document.createElement("li");

    listItem.innerHTML = `
      <a href="${restaurant.url}" target="_blank" style="text-decoration: none; color: inherit;">
        <h3>${restaurant.name}</h3>
        <p>Rating: ${restaurant.rating}</p>
        <p>Address: ${restaurant.location.address1}, ${restaurant.location.city}, ${restaurant.location.state} ${restaurant.location.zip_code}</p>
      </a>
    `;

    resultsElement.appendChild(listItem);
  }
}
