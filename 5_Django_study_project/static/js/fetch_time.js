
function fetchTime() {
fetch('/server_time/')  // Replace with the actual path
  .then(response => response.text())
  .then(html => {
    document.getElementById('time-container').innerHTML = html;
  })
  .catch(error => console.error('Error fetching time:', error));
}

// Fetch time every second
setInterval(fetchTime, 1000);

