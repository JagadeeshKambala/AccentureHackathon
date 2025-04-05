const API_BASE_URL = "http://localhost:8000/api";

async function postData(endpoint, formData) {
  try {
    const response = await fetch(`${API_BASE_URL}/${endpoint}`, {
      method: "POST",
      body: formData,
    });

    const contentType = response.headers.get("content-type");

    if (!response.ok) {
      const errorData =
        contentType && contentType.includes("application/json")
          ? await response.json()
          : await response.text();
      throw new Error(errorData.message || JSON.stringify(errorData));
    }

    return await response.json();
  } catch (error) {
    throw new Error(error.message || "Network error");
  }
}
