// Simulated statistics for demonstration purposes.
let simulatedStatistics = {
    likes: 1100,
    comments: 3,
    shares: 70,
    views: 100000,
};

// Function to update the statistics on the page.
function updateStatistics() {
    document.getElementById("likes").textContent = simulatedStatistics.likes;
    document.getElementById("comments").textContent = simulatedStatistics.comments;
    document.getElementById("shares").textContent = simulatedStatistics.shares;
    document.getElementById("views").textContent = simulatedStatistics.views;
}

// Load the initial statistics.
updateStatistics();

// Function to simulate updating statistics in real-time.
function simulateRealTimeUpdates() {
    setInterval(() => {
        // Simulate updates by adding random values.
        simulatedStatistics.likes += Math.floor(Math.random() * 10);
        simulatedStatistics.comments += Math.floor(Math.random() * 0);
        simulatedStatistics.shares += Math.floor(Math.random() * 2);
        simulatedStatistics.views += Math.floor(Math.random() * 100);

        // Update the displayed statistics.
        updateStatistics();
    }, 5000); // Update every 5 seconds.
}

// Start simulating real-time updates.
simulateRealTimeUpdates();

// Login button click event handler (simulated login).
document.getElementById("login-button").addEventListener("click", function () {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    // Simulated login logic (replace with real authentication).
    if (username === "username" && password === "password") {
        alert("Login successful!");
        document.getElementById("dashboard").style.display = "block";
        document.getElementById("login-section").style.display = "none";
        document.getElementById("logout-button").style.display = "block";
    } else {
        alert("Login failed. Please check your credentials.");
    }
});

// Logout button click event handler.
document.getElementById("logout-button").addEventListener("click", function () {
    document.getElementById("dashboard").style.display = "none";
    document.getElementById("login-section").style.display = "block";
    document.getElementById("logout-button").style.display = "none";
});
