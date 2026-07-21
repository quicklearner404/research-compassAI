import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { createSession } from "../services/api";

export default function NewResearch() {
  const [prompt, setPrompt] = useState("");
  const [loading, setLoading] = useState(false);

  const navigate = useNavigate();

  async function handleStartResearch() {
    if (!prompt.trim()) return;

    try {
      setLoading(true);

      const session = await createSession(prompt);

      navigate(`/chat/${session.id}`);

    } catch (error) {
      console.error(error);
      alert("Failed to create research session.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="flex h-screen items-center justify-center bg-slate-50">

      <div className="w-full max-w-2xl px-6">

        <h1 className="mb-8 text-center text-4xl font-bold">
          New Research
        </h1>

        <div className="flex gap-3">

          <input
            className="flex-1 rounded-xl border px-5 py-4 outline-none focus:border-blue-500"
            placeholder="What would you like to research?"
            value={prompt}
            onChange={(e) => setPrompt(e.target.value)}
            onKeyDown={(e) => {
              if (e.key === "Enter") {
                handleStartResearch();
              }
            }}
          />

          <button
            onClick={handleStartResearch}
            disabled={loading}
            className="rounded-xl bg-blue-600 px-6 py-4 text-white hover:bg-blue-700 disabled:opacity-50"
          >
            {loading ? "Starting..." : "Start"}
          </button>

        </div>

      </div>

    </div>
  );
}