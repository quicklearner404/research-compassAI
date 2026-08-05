import { useEffect, useRef, useState } from "react";
import { useLocation, useParams } from "react-router-dom";

import {
  getSession,
  getMessages,
  chat,
} from "../services/api";

import ChatHeader from "../components/chat/ChatHeader";
import MessageList from "../components/chat/MessageList";
import MessageInput from "../components/chat/MessageInput";
import { shouldProcessInitialQuery } from "../utils/initialQueryGuard";

export default function Chat() {
  const { sessionId } = useParams();
  const location = useLocation();
  const processedInitialQueriesRef = useRef(new Set());

  const [session, setSession] = useState(null);
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(true);

  const messagesContainerRef = useRef(null);

  useEffect(() => {
    loadConversation();
  }, [sessionId]);

  useEffect(() => {
    if (messagesContainerRef.current) {
      messagesContainerRef.current.scrollTop =
        messagesContainerRef.current.scrollHeight;
    }
  }, [messages]);

  useEffect(() => {
    if (loading) return;

    const initialQuery = location.state?.initialQuery;
    const locationKey = `${sessionId}-${location.key}`;

    if (initialQuery && shouldProcessInitialQuery(locationKey, processedInitialQueriesRef.current)) {
      handleSend(initialQuery);

      // Prevent duplicate send on refresh
      window.history.replaceState({}, "");
    }
  }, [loading, location.key, location.state?.initialQuery, sessionId]);

  async function loadConversation() {
    try {
      const sessionData = await getSession(sessionId);
      const messageData = await getMessages(sessionId);

      setSession(sessionData);
      setMessages(Array.isArray(messageData) ? messageData : []);
    } catch (error) {
      console.error(error);
    } finally {
      setLoading(false);
    }
  }

  async function handleSend(text) {
    const tempUser = {
      id: `temp-user-${Date.now()}`,
      role: "user",
      content: text,
    };

    const tempAssistant = {
      id: `temp-assistant-${Date.now()}`,
      role: "assistant",
      content: "",
      loading: true,
    };

    // Optimistic UI
    setMessages((prev) => [
      ...prev,
      tempUser,
      tempAssistant,
    ]);

    // Allow React to paint the optimistic message
    await new Promise((resolve) =>
      requestAnimationFrame(resolve)
    );

    try {
      await chat(sessionId, text);

      const updatedMessages = await getMessages(sessionId);

      setMessages(updatedMessages);
    } catch (error) {
      console.error(error);

      setMessages((prev) =>
        prev.map((msg) =>
          msg.id === tempAssistant.id
            ? {
                ...msg,
                loading: false,
                content: "Something went wrong. Please try again.",
              }
            : msg
        )
      );
    }
  }

  if (loading) {
    return (
      <div className="flex h-screen items-center justify-center">
        Loading...
      </div>
    );
  }

  if (!session) {
    return (
      <div className="flex h-screen items-center justify-center text-slate-600">
        Unable to load this conversation.
      </div>
    );
  }

  return (
    <div className="flex h-screen flex-col bg-slate-50">
      <ChatHeader title={session.title || "Conversation"} />

      <div
        ref={messagesContainerRef}
        className="flex-1 overflow-y-auto"
      >
        <MessageList messages={messages} />
      </div>

      <MessageInput onSend={handleSend} />
    </div>
  );
}