import { ArrowRight, Search } from "lucide-react";

export default function SearchBox() {
  return (
    <div className="mx-auto mt-8 max-w-4xl">
      <div className="flex items-center rounded-2xl border border-gray-200 bg-white px-4 py-4 shadow-sm transition-all duration-300 hover:shadow-md sm:px-6">
        <Search size={20} className="text-gray-400" />

        <input
          className="ml-4 flex-1 text-lg text-gray-700 outline-none"
          placeholder="Describe your research problem..."
        />

        <button className="ml-4 inline-flex items-center rounded-xl bg-blue-600 px-5 py-3 font-semibold text-white transition-all duration-300 hover:scale-105 hover:bg-blue-700 sm:ml-5">
          Start Research
          <ArrowRight size={16} className="ml-2" />
        </button>
      </div>
    </div>
  );
}