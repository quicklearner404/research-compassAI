const topics = ["Agentic AI", "RAG", "Multimodal LLMs", "Vision Transformers", "Medical Imaging"];

export default function TrendingTopics() {
  return (
    <section className="rounded-[24px] border border-slate-200 bg-white p-6 shadow-sm">
      <div className="flex items-center justify-between">
        <div>
          <h2 className="text-lg font-semibold text-slate-900">Trending Research Topics</h2>
          <p className="text-sm text-slate-500">Topics gaining momentum in the research community.</p>
        </div>
      </div>

      <div className="mt-4 flex flex-wrap gap-2">
        {topics.map((topic) => (
          <span key={topic} className="rounded-full border border-slate-200 bg-white px-3 py-1.5 text-sm text-slate-600">
            {topic}
          </span>
        ))}
      </div>
    </section>
  );
}