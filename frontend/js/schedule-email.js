document.getElementById("emailForm").addEventListener("submit", async (e) => {
  e.preventDefault();
  const formData = new FormData(e.target);
  const resultDiv = document.getElementById("emailOutput");

  try {
    const response = await postData("schedule-interview", formData);
    const { name, email, job_title, interview_time, interview_location } =
      response.data;

    resultDiv.textContent = `Interview Scheduled Successfully 🎉

Name: ${name}
Email: ${email}
Job Title: ${job_title}
Time: ${interview_time}
Location: ${interview_location}`;
    resultDiv.classList.remove("d-none");
  } catch (err) {
    resultDiv.textContent = "Error: " + err.message;
    resultDiv.classList.remove("d-none");
  }
});
