
function fetchTime() {
fetch('/server_time/')
  .then(response => response.text())
  .then(html => {
    document.getElementById('time-container').innerHTML = html;
  })
  .catch(error => console.error('Error fetching time:', error));
}


setInterval(fetchTime, 1000);

