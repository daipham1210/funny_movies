// logging key-value pairs of FormData object
function logFormData(data) {
  for (const pair of data.entries()) {
    console.log(pair[0] + ": " + pair[1]);
  }
}

function alertMsg(msg) {
  const messages = document.getElementById("messages-list");
  messages.innerHTML += '<div class="alert alert-error msg fade show" role="alert">' + msg + '</div>';
  fadeAlerts();
}

// fade out message alerts
function fadeAlerts() {
  alerts = document.getElementsByClassName("alert msg");
  var i = alerts.length;
  for (let elem of alerts) {
    i--;
    time = 3250+(1000*i);
    setTimeout(function() {
        $(elem).fadeOut("slow");
    }, time);
  }
}

// call fade out after DOMContentLoaded
window.addEventListener('DOMContentLoaded', (event) => {
  fadeAlerts();
});