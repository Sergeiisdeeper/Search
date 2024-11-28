const canvas = document.getElementById("gameCanvas");
const ctx = canvas.getContext("2d");

// Game logic here
function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.fillStyle = "white";
    ctx.fillRect(10, 10, 50, 50); // Example rectangle
}

setInterval(draw, 100);
