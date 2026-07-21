import { useState } from "react";
import { Bookmark, ChevronLeft, ChevronRight, Clock3, LayoutGrid, PlusCircle, Settings } from "lucide-react";
import { NavLink } from "react-router-dom";
import { useAuth } from "../../context/AuthContext";

const navItems = [
  { label: "Dashboard", icon: LayoutGrid, to: "/dashboard" },
  { label: "New Research", icon: PlusCircle, to: "/new" },
  { label: "History", icon: Clock3, to: "/history" },
  { label: "Saved", icon: Bookmark, to: "/saved" },
  { label: "Settings", icon: Settings, to: "/settings" },
];

export default function Sidebar() {
  const [collapsed, setCollapsed] = useState(false);
  const { currentUser } = useAuth();

  const displayName = currentUser?.displayName || "Research User";
  const email = currentUser?.email || "Signed in with Google";
  const initials = displayName
    .split(" ")
    .slice(0, 2)
    .map((part) => part[0])
    .join("")
    .toUpperCase();

  return (
    <aside className={`flex flex-col border-r border-slate-200 bg-white px-4 py-6 transition-all duration-200 ${collapsed ? "w-[84px]" : "w-[270px]"}`}>
      <div className="flex items-center justify-between">
        <div className={`flex items-center gap-3 ${collapsed ? "justify-center" : ""}`}>
          <div className="flex h-11 w-11 items-center justify-center rounded-2xl bg-blue-600 text-white shadow-sm">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" className="h-5 w-5">
              <path d="m21 21-4.35-4.35" />
              <circle cx="11" cy="11" r="6" />
            </svg>
          </div>
          {!collapsed && (
            <div>
              <p className="text-sm font-semibold text-slate-900">Research Compass AI</p>
              <p className="text-xs text-slate-500">AI Research Assistant</p>
            </div>
          )}
        </div>
        <button onClick={() => setCollapsed((value) => !value)} className="rounded-full border border-slate-200 bg-white p-1.5 text-slate-500 hover:bg-slate-50">
          {collapsed ? <ChevronRight size={16} /> : <ChevronLeft size={16} />}
        </button>
      </div>

      <nav className="mt-8 space-y-1">
        {navItems.map(({ label, icon: Icon, to }) => (
          <NavLink
            key={label}
            to={to}
            className={({ isActive }) =>
              [
                "flex items-center rounded-2xl px-3 py-2.5 text-sm font-medium transition-colors",
                collapsed ? "justify-center" : "gap-3",
                isActive ? "bg-blue-600 text-white shadow-sm" : "text-slate-600 hover:bg-blue-50 hover:text-blue-700",
              ].join(" ")
            }
          >
            {({ isActive }) => (
              <>
                <Icon size={18} className={isActive ? "text-white" : "text-slate-400"} />
                {!collapsed && <span>{label}</span>}
              </>
            )}
          </NavLink>
        ))}
      </nav>

      <div className="mt-auto rounded-2xl border border-slate-200 bg-slate-50 p-3">
        <div className={`flex items-center ${collapsed ? "justify-center" : "gap-3"}`}>
          <div className="flex h-10 w-10 items-center justify-center rounded-full bg-blue-600 text-sm font-semibold text-white">
            {initials}
          </div>
          {!collapsed && (
            <div className="min-w-0">
              <p className="truncate text-sm font-semibold text-slate-900">{displayName}</p>
              <p className="truncate text-xs text-slate-500">{email}</p>
            </div>
          )}
        </div>
      </div>
    </aside>
  );
}
