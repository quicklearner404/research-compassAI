import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";

export default function MessageBubble({ role, content, loading }) {
  const isUser = role === "user";
  const safeContent = typeof content === "string" ? content : "";

  if (loading) {
    return (
      <div className="max-w-3xl rounded-2xl border border-slate-200 bg-white px-5 py-4 italic text-slate-500 animate-pulse">
        Thinking...
      </div>
    );
  }

  return (
    <div
      className={`prose prose-slate max-w-3xl rounded-2xl px-5 py-4 ${
        isUser
          ? "ml-auto bg-blue-600 text-white"
          : "bg-white border border-slate-200"
      }`}
    >
      <ReactMarkdown remarkPlugins={[remarkGfm]}>{safeContent}</ReactMarkdown>
    </div>
  );
}