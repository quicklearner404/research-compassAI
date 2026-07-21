import { ArrowRight, BookOpen, GitBranch, NotebookPen } from "lucide-react";

const actions = [
  { title: "Research Papers", description: "Find the latest studies and cite-worthy sources.", icon: BookOpen },
  { title: "GitHub Projects", description: "Inspect implementation details and code examples.", icon: GitBranch },
  { title: "Learning Roadmaps", description: "Build a guided path from theory to practice.", icon: NotebookPen },
];

export default function QuickActions() {
  return (
    <section className="rounded-[24px] border border-slate-200 bg-white p-6 shadow-sm">
      <div className="flex items-center justify-between">
        <div>
          <h2 className="text-lg font-semibold text-slate-900">Quick Actions</h2>
          <p className="text-sm text-slate-500">Start with the most useful next step.</p>
        </div>
      </div>

      <div className="mt-6 space-y-3">
        {actions.map(({ title, description, icon: Icon }) => (
          <button
            key={title}
            className="flex w-full items-center justify-between rounded-2xl border border-slate-200 bg-white px-4 py-3 text-left transition hover:border-blue-200 hover:bg-blue-50"
          >
            <div className="flex items-center gap-3">
              <div className="flex h-10 w-10 items-center justify-center rounded-2xl bg-blue-50 text-blue-600">
                <Icon size={18} />
              </div>
              <div>
                <p className="text-sm font-semibold text-slate-900">{title}</p>
                <p className="text-sm text-slate-500">{description}</p>
              </div>
            </div>
            <ArrowRight size={16} className="text-slate-400" />
          </button>
        ))}
      </div>
    </section>
  );
}