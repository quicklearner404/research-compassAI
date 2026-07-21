import { Search, GitBranch } from "lucide-react";
import { useAuth } from "../../context/AuthContext";
export default function Navbar() {
  const { currentUser, login, logout } = useAuth();
  return (
    <nav className="w-full border-b border-gray-200 bg-white/95">
      <div className="mx-auto flex h-20 max-w-7xl items-center justify-between px-4 sm:px-6 lg:px-8">
        <div className="flex items-center gap-3">
          <div className="flex h-11 w-11 items-center justify-center rounded-xl bg-blue-600 text-white font-bold transition duration-300 hover:rotate-6">
            <Search size={20} />
          </div>

          <div>
            <h1 className="text-xl font-bold text-gray-900">Research Compass AI</h1>
            <p className="text-sm text-gray-500">Your AI Research Assistant</p>
          </div>
        </div>

        <div className="hidden items-center gap-10 text-gray-600 md:flex">
          <a href="#" className="transition hover:text-blue-600">
            Documentation
          </a>

          <a href="#" className="flex items-center gap-2 transition hover:text-blue-600">
            <GitBranch size={18} />
            GitHub
          </a>
        </div>

 {currentUser ? (
    <div className="flex items-center gap-3">

        <img
            src={currentUser.photoURL}
            alt={currentUser.displayName}
            className="h-10 w-10 rounded-full border border-gray-300"
        />

        <button
            onClick={logout}
            className="rounded-xl border border-gray-300 px-4 py-2 text-sm hover:bg-gray-100"
        >
            Logout
        </button>

    </div>
) : (

    <button
        onClick={login}
        className="rounded-xl bg-blue-600 px-4 py-2.5 font-medium text-white transition-all duration-300 hover:scale-105 hover:bg-blue-700"
    >
        Sign In
    </button>

)}
      </div>
    </nav>
  );
}