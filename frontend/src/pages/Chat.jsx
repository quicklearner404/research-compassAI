import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { getSession } from "../services/api";

export default function Chat() {
  const { sessionId } = useParams();

  const [session, setSession] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function loadSession() {
      try {
        const data = await getSession(sessionId);
        setSession(data);
      } catch (error) {
        console.error(error);
      } finally {
        setLoading(false);
      }
    }

    loadSession();
  }, [sessionId]);

  if (loading) {
    return (
      <div className="flex h-screen items-center justify-center">
        Loading...
      </div>
    );
  }

  return (
    <div className="p-10">

      <h1 className="text-4xl font-bold">
        {session.title}
      </h1>

      <p className="mt-2 text-slate-500">
        Session #{session.id}
      </p>

      <div className="mt-12 rounded-xl border border-dashed border-slate-300 p-8 text-center text-slate-500">
        Chat interface coming next...
      </div>

    </div>
  );
}