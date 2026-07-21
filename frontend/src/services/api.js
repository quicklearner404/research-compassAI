const BASE_URL = import.meta.env.VITE_API_URL?.replace(/\/$/, "") || "http://127.0.0.1:8000";

function getSessionPath(sessionId) {
  return encodeURIComponent(String(sessionId));
}

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
    `${BASE_URL}/sessions/${getSessionPath(id)}`
  );

  if (!response.ok) {
    throw new Error("Failed to load session");
  }

  return response.json();
}
export async function getMessages(sessionId) {
  const response = await fetch(
    `${BASE_URL}/sessions/${getSessionPath(sessionId)}/messages`
  );

  if (!response.ok) {
    throw new Error("Failed to load messages");
  }

  return response.json();
}

export async function createMessage(sessionId, role, content) {
  const response = await fetch(
    `${BASE_URL}/sessions/${getSessionPath(sessionId)}/messages`,
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        role,
        content,
      }),
    }
  );

  if (!response.ok) {
    throw new Error("Failed to create message");
  }

  return response.json();
}