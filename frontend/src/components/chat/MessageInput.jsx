import { useState } from "react";

export default function MessageInput({ onSend }) {
  const [text, setText] = useState("");

  async function handleSubmit(event) {
    event.preventDefault();

    const trimmedText = text.trim();
    if (!trimmedText || typeof onSend !== "function") {
      return;
    }

    await onSend(trimmedText);
    setText("");
  }

  return (
    <form onSubmit={handleSubmit} className="border-t border-slate-200 bg-white p-4">
      <div className="mx-auto flex max-w-3xl gap-3">
        <input
          type="text"
          value={text}
          onChange={(event) => setText(event.target.value)}
          placeholder="Type your message..."
          className="flex-1 rounded-full border border-slate-200 bg-slate-50 px-4 py-3 text-sm outline-none ring-0 focus:border-blue-500 focus:bg-white"
        />
        <button
          type="submit"
          className="rounded-full bg-blue-600 px-4 py-3 text-sm font-semibold text-white transition hover:bg-blue-700"
        >
          Send
        </button>
      </div>
    </form>
  );
}