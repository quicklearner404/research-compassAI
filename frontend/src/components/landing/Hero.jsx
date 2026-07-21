export default function Hero() {
  return (
    <section className="pt-8 text-center sm:pt-10 lg:pt-12">
      <div className="inline-flex items-center rounded-full border border-blue-200 bg-blue-50 px-4 py-1.5 text-sm font-medium text-blue-700">
        AI-powered research companion • Beta
      </div>

      <h1 className="mt-5 text-4xl font-extrabold tracking-tight text-gray-900 sm:text-5xl lg:text-6xl">
        Navigate Research
        <br />
        With Confidence
      </h1>

      <p className="mx-auto mt-4 max-w-2xl text-lg leading-8 text-gray-600 sm:text-xl">
        Discover papers, repositories, tutorials, and learning resources
        powered by AI. Organize everything in one place.
      </p>
    </section>
  );
}