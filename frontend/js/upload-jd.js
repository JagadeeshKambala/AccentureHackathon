document.getElementById("jdForm").addEventListener("submit", async (e) => {
  e.preventDefault();
  const jdText = document.getElementById("jdText").value;

  const response = await fetch("http://localhost:8000/api/upload-jd", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ text: jdText }),
  });

  const data = await response.json();
  document.getElementById("result").textContent = JSON.stringify(data, null, 2);
});
