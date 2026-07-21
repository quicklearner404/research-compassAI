import { BookOpen, Compass, GitBranch } from "lucide-react";

export default function FeatureCard({ title, description, icon: Icon }) {
  const iconClass = "h-12 w-12 rounded-xl bg-blue-50 text-blue-600";

  return (
    <div className="flex h-full flex-col rounded-2xl border border-gray-200 bg-white p-6 shadow-sm transition-all duration-300 hover:-translate-y-1 hover:shadow-xl">
      <div className={`mb-4 inline-flex items-center justify-center ${iconClass}`}>
        {Icon ? <Icon size={20} /> : <BookOpen size={20} />}
      </div>

      <h3 className="text-xl font-semibold text-gray-900">{title}</h3>

      <p className="mt-3 flex-1 text-gray-600 leading-7">{description}</p>
    </div>
  );
}