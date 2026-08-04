import { useEffect, useState } from "react";
import {
  NavLink,
  useNavigate,
  useLocation,
} from "react-router-dom";
import {
  Bookmark,
  ChevronLeft,
  ChevronRight,
  LayoutGrid,
  PlusCircle,
  Settings,
} from "lucide-react";

import { useAuth } from "../../context/AuthContext";
import { getSessions } from "../../services/api";

const navItems = [
  { label: "Dashboard", icon: LayoutGrid, to: "/dashboard" },
  { label: "New Research", icon: PlusCircle, to: "/new" },
  { label: "Saved", icon: Bookmark, to: "/saved" },
  { label: "Settings", icon: Settings, to: "/settings" },
];

export default function Sidebar() {
  const [collapsed, setCollapsed] = useState(false);
  const [sessions, setSessions] = useState([]);
  const [loadingSessions, setLoadingSessions] = useState(true);

  const { currentUser } = useAuth();
  const navigate = useNavigate();
  const location = useLocation();

  const displayName = currentUser?.displayName || "Research User";
  const email = currentUser?.email || "Signed in with Google";

  const initials = displayName
    .split(" ")
    .slice(0, 2)
    .map((part) => part[0])
    .join("")
    .toUpperCase();

  useEffect(() => {
    async function loadSessions() {
      try {
        const data = await getSessions();
        setSessions(data);
      } catch (error) {
        console.error("Failed to load sessions:", error);
      } finally {
        setLoadingSessions(false);
      }
    }

    loadSessions();
  }, []);

  return (
    <aside
      className={`flex h-screen flex-col border-r border-slate-200 bg-white px-4 py-6 transition-all duration-200 ${
        collapsed ? "w-[84px]" : "w-[270px]"
      }`}
    >
      {/* Logo */}
      <div className="flex items-center justify-between">
        <div
          className={`flex items-center gap-3 ${
            collapsed ? "justify-center" : ""
          }`}
        >
          <div className="flex h-11 w-11 items-center justify-center rounded-2xl bg-blue-600 text-white shadow-sm">
            <svg
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              strokeWidth="2"
              className="h-5 w-5"
            >
              <path d="m21 21-4.35-4.35" />
              <circle cx="11" cy="11" r="6" />
            </svg>
          </div>

          {!collapsed && (
            <div>
              <p className="text-sm font-semibold text-slate-900">
                Research Compass AI
              </p>
              <p className="text-xs text-slate-500">
                AI Research Assistant
              </p>
            </div>
          )}
        </div>

        <button
          onClick={() => setCollapsed((value) => !value)}
          className="rounded-full border border-slate-200 bg-white p-1.5 text-slate-500 hover:bg-slate-50"
        >
          {collapsed ? (
            <ChevronRight size={16} />
          ) : (
            <ChevronLeft size={16} />
          )}
        </button>
      </div>

      {/* Navigation */}
      <nav className="mt-8 space-y-1">
        {navItems.map(({ label, icon: Icon, to }) => (
          <NavLink
            key={label}
            to={to}
            className={({ isActive }) =>
              [
                "flex items-center rounded-2xl px-3 py-2.5 text-sm font-medium transition-colors",
                collapsed ? "justify-center" : "gap-3",
                isActive
                  ? "bg-blue-600 text-white shadow-sm"
                  : "text-slate-600 hover:bg-blue-50 hover:text-blue-700",
              ].join(" ")
            }
          >
            {({ isActive }) => (
              <>
                <Icon
                  size={18}
                  className={
                    isActive ? "text-white" : "text-slate-400"
                  }
                />
                {!collapsed && <span>{label}</span>}
              </>
            )}
          </NavLink>
        ))}
      </nav>

      {/* Sessions */}
      <div className="mt-8 flex-1 overflow-y-auto">
        {!collapsed && (
          <h3 className="mb-3 px-2 text-xs font-semibold uppercase tracking-[0.15em] text-slate-500">
            Recent Sessions
          </h3>
        )}

        {loadingSessions ? (
          <p className="px-2 text-sm text-slate-500">
            Loading...
          </p>
        ) : sessions.length === 0 ? (
          <div className="rounded-xl bg-slate-100 p-3 text-sm text-slate-500">
            No sessions yet.
          </div>
        ) : (
          <div className="space-y-2">
            {sessions.map((session) => {
              const isActive =
                location.pathname === `/chat/${session.id}`;

              return (
                <button
                  key={session.id}
                  onClick={() => navigate(`/chat/${session.id}`)}
                  className={`w-full rounded-xl px-3 py-2 text-left transition ${
                    collapsed ? "flex justify-center" : ""
                  } ${
                    isActive
                      ? "bg-blue-600 text-white shadow-sm"
                      : "hover:bg-slate-100"
                  }`}
                >
                  {collapsed ? (
                    <svg
                      viewBox="0 0 24 24"
                      fill="none"
                      stroke="currentColor"
                      strokeWidth="2"
                      className={`h-4 w-4 ${
                        isActive
                          ? "text-white"
                          : "text-slate-500"
                      }`}
                    >
                      <path d="m21 21-4.35-4.35" />
                      <circle cx="11" cy="11" r="6" />
                    </svg>
                  ) : (
                    <>
                      <p
                        className={`truncate text-sm font-medium ${
                          isActive
                            ? "text-white"
                            : "text-slate-800"
                        }`}
                      >
                        {session.title}
                      </p>

                      <p
                        className={`text-xs ${
                          isActive
                            ? "text-blue-100"
                            : "text-slate-500"
                        }`}
                      >
                        Session #{session.id}
                      </p>
                    </>
                  )}
                </button>
              );
            })}
          </div>
        )}
      </div>

      {/* Account */}
      <div className="mt-4 rounded-2xl border border-slate-200 bg-slate-50 p-3">
        <div
          className={`flex items-center ${
            collapsed ? "justify-center" : "gap-3"
          }`}
        >
          <div className="flex h-10 w-10 items-center justify-center rounded-full bg-blue-600 text-sm font-semibold text-white">
            {initials}
          </div>

          {!collapsed && (
            <div className="min-w-0">
              <p className="truncate text-sm font-semibold text-slate-900">
                {displayName}
              </p>
              <p className="truncate text-xs text-slate-500">
                {email}
              </p>
            </div>
          )}
        </div>
      </div>
    </aside>
  );
}