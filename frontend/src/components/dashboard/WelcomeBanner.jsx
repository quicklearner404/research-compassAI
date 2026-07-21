import { useAuth } from "../../context/AuthContext";

export default function WelcomeBanner() {
  const { currentUser } = useAuth();
  const firstName = currentUser?.displayName?.split(" ")[0] || "there";

  return (
    <section className="rounded-[24px] border border-slate-200 bg-white p-6 shadow-sm lg:p-7">
      <div className="max-w-2xl">
        <h2 className="text-[28px] font-semibold leading-tight text-slate-900">
          Good morning, {firstName}.
        </h2>
        <p className="mt-2 text-[15px] leading-7 text-slate-600">
          Ready to continue your research?
        </p>
      </div>
    </section>
  );
}