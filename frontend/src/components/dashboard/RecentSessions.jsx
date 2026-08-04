import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

import { getSessions } from "../../services/api";

export default function RecentSessions() {
  const [sessions, setSessions] = useState([]);
  const [loading, setLoading] = useState(true);

  const navigate = useNavigate();

  useEffect(() => {
    async function loadSessions() {
      try {
        const data = await getSessions();
        setSessions(data);
      } catch (error) {
        console.error("Failed to load sessions:", error);
      } finally {
        setLoading(false);
      }
    }

    loadSessions();
  }, []);

  // Show only the 3 most recent sessions
  const recentSessions = sessions.slice(0, 3);

  return (
    <section className="rounded-[24px] border border-slate-200 bg-white p-6 shadow-sm">
      <div className="flex items-center justify-between">
        <div>
          <h2 className="text-lg font-semibold text-slate-900">
            Continue working
          </h2>
          <p className="text-sm text-slate-500">
            Pick up where you left off.
          </p>
        </div>
      </div>

      <div className="mt-6">
        {loading ? (
          <p className="text-sm text-slate-500">
            Loading sessions...
          </p>
        ) : recentSessions.length === 0 ? (
          <div className="rounded-2xl border border-dashed border-slate-300 bg-slate-50 p-6 text-center">
            <p className="text-sm font-medium text-slate-700">
              No research sessions yet.
            </p>
            <p className="mt-2 text-sm text-slate-500">
              Start your first research conversation to build your library.
            </p>
          </div>
        ) : (
          <div className="space-y-3">
            {recentSessions.map((session) => (
              <button
                key={session.id}
                onClick={() => navigate(`/chat/${session.id}`)}
                className="flex w-full items-center justify-between rounded-2xl border border-slate-200 bg-slate-50 px-4 py-3 text-left transition hover:border-blue-200 hover:bg-blue-50"
              >
                <div>
                  <p className="text-sm font-semibold text-slate-900">
                    {session.title}
                  </p>

                  <p className="text-sm text-slate-500">
                    Session #{session.id}
                  </p>
                </div>

                <span className="rounded-full border border-slate-200 bg-white px-3 py-1.5 text-xs font-semibold uppercase tracking-[0.15em] text-slate-600">
                  Open →
                </span>
              </button>
            ))}
          </div>
        )}
      </div>
    </section>
  );
}