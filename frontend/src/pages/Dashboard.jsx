import { useState } from "react";
import { Search } from "lucide-react";
import { useNavigate } from "react-router-dom";

import DashboardLayout from "../components/dashboard/DashboardLayout";
import WelcomeBanner from "../components/dashboard/WelcomeBanner";
import QuickActions from "../components/dashboard/QuickActions";
import RecentSessions from "../components/dashboard/RecentSessions";
import TrendingTopics from "../components/dashboard/TrendingTopics";

import {
  createSession,
  chat,
} from "../services/api";

export default function Dashboard() {
  const [query, setQuery] = useState("");
  const navigate = useNavigate();

  const handleStartResearch = async () => {
    if (!query.trim()) return;

    try {
      const title =
        query.length > 50
          ? `${query.slice(0, 50)}...`
          : query;

      // Create session
      const session = await createSession(title);

      // Send first message
      await chat(session.id, query);

      // Clear input
      setQuery("");

      // Open chat page
      navigate(`/chat/${session.id}`);
    } catch (error) {
      console.error("Failed to start research session:", error);
    }
  };

  return (
    <DashboardLayout>
      <WelcomeBanner />

      <section className="rounded-[24px] border border-slate-200 bg-white p-6 shadow-sm lg:p-8">
        <div className="mx-auto flex max-w-3xl flex-col items-center text-center">
          <p className="text-[12px] font-semibold uppercase tracking-[0.2em] text-blue-600">
            Start a New Research Session
          </p>

          <h3 className="mt-2 text-[24px] font-semibold leading-tight text-slate-900">
            What would you like to research today?
          </h3>

          <p className="mt-2 text-[14px] leading-6 text-slate-500">
            Ask questions, compare papers, explore technologies, or begin a
            literature review.
          </p>

          <div className="mt-6 flex w-full items-center rounded-2xl border border-slate-200 bg-slate-50 px-4 py-3.5 shadow-sm">
            <Search
              size={18}
              className="text-slate-400"
            />

            <input
              type="text"
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              onKeyDown={(e) => {
                if (e.key === "Enter") {
                  handleStartResearch();
                }
              }}
              placeholder="Ask your research question..."
              className="ml-3 w-full bg-transparent text-[14px] text-slate-700 outline-none"
            />

            <button
              onClick={handleStartResearch}
              disabled={!query.trim()}
              className="ml-3 rounded-2xl bg-blue-600 px-5 py-2.5 text-[14px] font-semibold text-white transition hover:bg-blue-700 disabled:cursor-not-allowed disabled:bg-slate-300"
            >
              Start Research
            </button>
          </div>
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