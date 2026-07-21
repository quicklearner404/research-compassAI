const BASE_URL = "http://127.0.0.1:8000";

export async function createSession(title) {
    const response = await fetch(`${BASE_URL}/sessions/`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            title,
        }),
    });

    if (!response.ok) {
        throw new Error("Failed to create session");
    }

    return response.json();
}
export async function getSession(id) {
  const response = await fetch(
    `${BASE_URL}/sessions/${id}`
  );

  if (!response.ok) {
    throw new Error("Failed to load session");
  }

  return response.json();
}