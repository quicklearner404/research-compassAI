import { BookOpen, Compass, GitBranch } from "lucide-react";

import Navbar from "../components/layout/Navbar";
import Hero from "../components/landing/Hero";
import SearchBox from "../components/landing/SearchBox";
import FeatureCards from "../components/landing/FeatureCards";

export default function Landing() {
  return (
    <div className="min-h-screen bg-gray-50">
      <Navbar />

      <div className="mx-auto max-w-7xl px-4 pb-16 sm:px-6 lg:px-8">
        <Hero />

        <SearchBox />

        <div className="mt-10 grid grid-cols-1 gap-6 md:grid-cols-3">
          <FeatureCards
            icon={BookOpen}
            title="Research Papers"
            description="Find the most relevant academic papers from trusted sources."
          />

          <FeatureCards
            icon={GitBranch}
            title="GitHub Projects"
            description="Discover implementations and open-source repositories."
          />

          <FeatureCards
            icon={Compass}
            title="Learning Roadmaps"
            description="Receive curated tutorials and step-by-step learning paths."
          />
        </div>

        <div className="mt-12 grid gap-4 rounded-2xl border border-gray-200 bg-white/80 p-6 shadow-sm sm:grid-cols-3">
          <div className="rounded-xl bg-gray-50 p-4">
            <div className="text-sm font-semibold uppercase tracking-[0.2em] text-blue-600">
              Search
            </div>

            <div className="mt-2 font-medium">
              Find papers, repos, and tutorials in one flow
            </div>
          </div>

          <div className="rounded-xl bg-gray-50 p-4">
            <div className="text-sm font-semibold uppercase tracking-[0.2em] text-blue-600">
              Organize
            </div>

            <div className="mt-2 font-medium">
              Turn scattered results into a structured research plan
            </div>
          </div>

          <div className="rounded-xl bg-gray-50 p-4">
            <div className="text-sm font-semibold uppercase tracking-[0.2em] text-blue-600">
              Learn
            </div>

            <div className="mt-2 font-medium">
              Get guided roadmaps and next steps without leaving the app
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}