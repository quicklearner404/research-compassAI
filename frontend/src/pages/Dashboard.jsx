import { Search } from "lucide-react";

import DashboardLayout from "../components/dashboard/DashboardLayout";
import WelcomeBanner from "../components/dashboard/WelcomeBanner";
import QuickActions from "../components/dashboard/QuickActions";
import RecentSessions from "../components/dashboard/RecentSessions";
import TrendingTopics from "../components/dashboard/TrendingTopics";

export default function Dashboard() {
  return (
    <DashboardLayout>
      <WelcomeBanner />

      <section className="rounded-[24px] border border-slate-200 bg-white p-6 shadow-sm lg:p-8">
        <div className="mx-auto flex max-w-3xl flex-col items-center text-center">
          <p className="text-[12px] font-semibold uppercase tracking-[0.2em] text-blue-600">Start a new inquiry</p>
          <h3 className="mt-2 text-[24px] font-semibold leading-tight text-slate-900">
            Search papers, technologies, datasets or research ideas...
          </h3>
          <p className="mt-2 text-[14px] leading-6 text-slate-500">
            Example: Survey papers on Retrieval-Augmented Generation or Vision Transformer vs Swin Transformer.
          </p>
          <div className="mt-6 flex w-full items-center rounded-2xl border border-slate-200 bg-slate-50 px-4 py-3.5 shadow-sm">
            <Search size={18} className="text-slate-400" />
            <input
              type="text"
              placeholder="Describe your research question..."
              className="ml-3 w-full bg-transparent text-[14px] text-slate-700 outline-none"
            />
            <button className="ml-3 rounded-2xl bg-blue-600 px-4 py-2.5 text-[14px] font-semibold text-white transition hover:bg-blue-700">
              Continue →
            </button>
          </div>
        </div>
      </section>

      <section className="rounded-[24px] border border-slate-200 bg-white p-6 shadow-sm">
        <div className="flex items-center justify-between">
          <div>
            <h2 className="text-lg font-semibold text-slate-900">Recent research</h2>
            <p className="text-sm text-slate-500">Pick up one of your latest investigations.</p>
          </div>
        </div>

        <div className="mt-5 space-y-3">
          {[
            "Transformer Architecture Review",
            "Vision Transformer Survey",
            "Medical Imaging Trends",
          ].map((item) => (
            <button key={item} className="flex w-full items-center justify-between rounded-2xl border border-slate-200 bg-slate-50 px-4 py-3 text-left transition hover:border-blue-200 hover:bg-blue-50">
              <span className="text-sm font-semibold text-slate-900">{item}</span>
              <span className="text-sm text-slate-500">Continue →</span>
            </button>
          ))}
        </div>
      </section>

      <div className="grid gap-6 xl:grid-cols-[1.15fr_0.85fr]">
        <RecentSessions />
        <QuickActions />
      </div>

      <TrendingTopics />
    </DashboardLayout>
  );
}