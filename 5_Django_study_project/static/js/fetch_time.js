// this is the javascript file that fetches the time from the server
function fetchTime() {
    // Fetch the current time from the server
    // /server_time/ is the path to the view that returns the time
    fetch('/server_time/')
        // When the response is received, convert it to text
      .then(response => response.text())
        // Then update the element containing the time
      .then(html => {
          // Select the element and update the html
        document.getElementById('time-container').innerHTML = html; // this is the id of the element that will be updated with the time
      })
        // If there's an error, log it to the console
      .catch(error => console.error('Error fetching time:', error));
    }
// Call fetchTime() once right now to display the time
setInterval(fetchTime, 1000);

