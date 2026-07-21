import { Search, Moon, Sun } from "lucide-react";
import { useTheme } from "../../context/ThemeContext";

export default function TopBar() {
  const { theme, toggleTheme } = useTheme();

  return (
    <header className="flex h-24 items-center justify-between border-b border-slate-200 bg-white px-6 lg:px-8">
      <div>
        <h1 className="text-[28px] font-semibold leading-tight text-slate-900">Research Workspace</h1>
      </div>

      <div className="flex items-center gap-3">
        <div className="relative hidden md:block">
          <Search size={18} className="absolute left-3 top-2.5 text-slate-400" />
          <input
            type="text"
            placeholder="Search sessions"
            className="w-72 rounded-2xl border border-slate-200 bg-slate-50 py-2.5 pl-10 pr-4 text-[14px] text-slate-700 outline-none transition focus:border-blue-500"
          />
        </div>

        <button
          onClick={toggleTheme}
          className="rounded-2xl border border-slate-200 bg-white p-2.5 text-slate-600 transition hover:bg-slate-50"
          aria-label="Toggle theme"
        >
          {theme === "dark" ? <Sun size={18} /> : <Moon size={18} />}
        </button>
      </div>
    </header>
  );
}