function updateDateTime() {
    var datetimeElement = document.getElementById("datetime");
    var now = new Date();
    datetimeElement.innerHTML = now.toLocaleString();
  }
  
  setInterval(updateDateTime, 1000); // Actualizar cada segundo