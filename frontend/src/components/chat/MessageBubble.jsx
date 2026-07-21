export default function MessageBubble({ role, content }) {
  const isUser = role === "user";

  return (
    <div
      className={`max-w-3xl rounded-2xl px-5 py-4 ${
        isUser
          ? "ml-auto bg-blue-600 text-white"
          : "bg-white border border-slate-200"
      }`}
    >
      {content}
    </div>
  );
}