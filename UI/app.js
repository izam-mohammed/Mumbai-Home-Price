// Function to retrieve the selected bath value
function getBathValue() {
  /**
   * Get the selected value of bathrooms.
   *
   * @returns {number} The selected bathroom value.
   */
  var uiBathrooms = document.getElementsByName("uiBathrooms");
  for (var i in uiBathrooms) {
    if (uiBathrooms[i].checked) {
      return parseInt(i) + 1;
    }
  }
  return -1; // Invalid Value
}

// Function to retrieve the selected BHK value
function getBHKValue() {
  /**
   * Get the selected value of BHK.
   *
   * @returns {number} The selected BHK value.
   */
  var uiBHK = document.getElementsByName("uiBHK");
  for (var i in uiBHK) {
    if (uiBHK[i].checked) {
      return parseInt(i) + 1;
    }
  }
  return -1; // Invalid Value
}

// Action when the estimate button is clicked
function onClickedEstimatePrice() {
  /**
   * Perform actions when the estimate price button is clicked.
   */
  console.log("Estimate price button clicked");
  var sqft = document.getElementById("uiSqft");
  var bhk = getBHKValue();
  var bathrooms = getBathValue();
  var location = document.getElementById("uiLocations");
  var estPrice = document.getElementById("uiEstimatedPrice");

  var url = "http://127.0.0.1:5000/predict_home_price";

  $.post(
    url,
    {
      total_sqft: parseFloat(sqft.value),
      bhk: bhk,
      bath: bathrooms,
      location: location.value,
    },
    function (data, status) {
      console.log(data.estimated_price);
      estPrice.innerHTML =
        "<h2>" + data.estimated_price.toString() + " Lakh</h2>";
      console.log(status);
    }
  );
}

// Load the page
function onPageLoad() {
  /**
   * Load necessary data when the page is loaded.
   */
  console.log("Document loaded");
  var url = "http://127.0.0.1:5000/get_location_names";
  $.get(url, function (data, status) {
    console.log("Got response for get_location_names request");
    if (data) {
      var locations = data.locations;
      var uiLocations = document.getElementById("uiLocations");
      $("#uiLocations").empty();
      for (var i in locations) {
        var opt = new Option(locations[i]);
        $("#uiLocations").append(opt);
      }
    }
  });
}

// Load data on window.onload
window.onload = onPageLoad;
