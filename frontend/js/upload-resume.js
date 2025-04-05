async function uploadResume(event) {
  event.preventDefault(); // prevent form from refreshing

  const form = document.getElementById("resumeForm");
  const resultBox = document.getElementById("result");

  const formData = new FormData(form);
  resultBox.textContent = "Uploading...";

  try {
    const response = await fetch("http://localhost:8000/api/upload-resume", {
      method: "POST",
      body: formData,
    });

    if (!response.ok) {
      const error = await response.json();
      resultBox.textContent = `❌ Error: ${JSON.stringify(error)}`;
      return;
    }

    const data = await response.json();
    resultBox.textContent = `✅ Resume uploaded successfully!\nMatch Score: ${data.match_score}`;

    // Keep the message visible for 5 minutes (300,000 ms)
    setTimeout(() => {
      resultBox.textContent = "";
    }, 300000); // 300,000 ms = 5 minutes
  } catch (err) {
    resultBox.textContent = `❌ Network error: ${err.message}`;
  }
}

window.addEventListener("DOMContentLoaded", () => {
  document
    .getElementById("resumeForm")
    .addEventListener("submit", uploadResume);
});
