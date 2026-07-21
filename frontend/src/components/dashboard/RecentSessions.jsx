const sessions = [
  { title: "Transformer Architecture Review", date: "Last opened 2 hours ago", status: "Resume" },
  { title: "Medical Imaging Trends", date: "Last opened yesterday", status: "Continue" },
  { title: "Graph Neural Networks", date: "Last opened 3 days ago", status: "Open" },
];

export default function RecentSessions() {
  return (
    <section className="rounded-[24px] border border-slate-200 bg-white p-6 shadow-sm">
      <div className="flex items-center justify-between">
        <div>
          <h2 className="text-lg font-semibold text-slate-900">Continue working</h2>
          <p className="text-sm text-slate-500">Pick up where you left off.</p>
        </div>
      </div>

      <div className="mt-6 space-y-3">
        {sessions.map((item) => (
          <div key={item.title} className="flex items-center justify-between rounded-2xl border border-slate-200 bg-slate-50 px-4 py-3">
            <div>
              <p className="text-sm font-semibold text-slate-900">{item.title}</p>
              <p className="text-sm text-slate-500">{item.date}</p>
            </div>
            <button className="rounded-full border border-slate-200 bg-white px-3 py-1.5 text-xs font-semibold uppercase tracking-[0.2em] text-slate-600">
              {item.status}
            </button>
          </div>
        ))}
      </div>
    </section>
  );
}