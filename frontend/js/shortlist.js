document
  .getElementById("shortlistForm")
  .addEventListener("submit", async (e) => {
    e.preventDefault();
    const jobId = document.getElementById("shortlistJobId").value;
    try {
      const response = await fetch(
        `http://localhost:8000/api/shortlist/${jobId}`
      );
      const data = await response.json();
      document.getElementById("shortlistResult").textContent = JSON.stringify(
        data,
        null,
        2
      );
    } catch (err) {
      document.getElementById("shortlistResult").textContent =
        "Error fetching shortlist: " + err.message;
    }
  });
