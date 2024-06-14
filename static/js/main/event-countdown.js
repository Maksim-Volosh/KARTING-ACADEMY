let next_event_time = document.getElementById("next_event_time").value;
console.log(next_event_time);

let parts = next_event_time.split(/[- :]/);
let eventDate = new Date(parts[0], parts[1] - 1, parts[2], parts[3], parts[4], parts[5]);

function eventCountdown() {
  let now = new Date();
  let difference = eventDate - now;

  if (difference > 0) {
    let days = Math.floor(difference / (1000 * 60 * 60 * 24));
    let hours = Math.floor((difference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    let minutes = Math.floor((difference % (1000 * 60 * 60)) / (1000 * 60));
    let seconds = Math.floor((difference % (1000 * 60)) / 1000);

    document.getElementById("countdown__days").innerText = `${days}`;
    document.getElementById("countdown__hours").innerText = `${hours}`;
    document.getElementById("countdown__mins").innerText = `${minutes}`;
    document.getElementById("countdown__secs").innerText = `${seconds}`;
  }
}

// Update the counter every second
let timer = setInterval(eventCountdown, 1000);
