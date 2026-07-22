import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
export default function MessageBubble({ role, content }) {
  const isUser = role === "user";
  console.log(content);
  return (
    <div
  className={`prose prose-slate max-w-3xl rounded-2xl px-5 py-4 ${
    isUser
      ? "ml-auto bg-blue-600 text-white"
      : "bg-white border border-slate-200"
  }`}
>
  <ReactMarkdown remarkPlugins={[remarkGfm]}>
    {content}
  </ReactMarkdown>
</div>
  );
}