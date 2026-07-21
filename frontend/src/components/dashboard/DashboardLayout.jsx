import Sidebar from "../layout/Sidebar";
import TopBar from "./TopBar";

export default function DashboardLayout({ children }) {
  return (
    <div className="flex min-h-screen bg-slate-50">
      <Sidebar />

      <div className="flex flex-1 flex-col">
        <TopBar />
        <main className="flex-1 overflow-hidden p-6 lg:p-8">
          <div className="mx-auto flex h-full max-w-7xl flex-col gap-6">{children}</div>
        </main>
      </div>
    </div>
  );
}