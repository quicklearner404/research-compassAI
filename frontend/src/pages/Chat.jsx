import { useEffect, useRef, useState } from "react";
import { useParams } from "react-router-dom";

import {
  getSession,
  getMessages,
  chat,
} from "../services/api";

import ChatHeader from "../components/chat/ChatHeader";
import MessageList from "../components/chat/MessageList";
import MessageInput from "../components/chat/MessageInput";

export default function Chat() {
  const { sessionId } = useParams();

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
      content: "Thinking...",
      loading: true,
    };

    // Immediately show user message + thinking bubble
    setMessages((prev) => [
      ...prev,
      tempUser,
      tempAssistant,
    ]);

    try {
      await chat(sessionId, text);

      const updatedMessages = await getMessages(sessionId);

      // Replace temporary messages with actual database messages
      setMessages(updatedMessages);
    } catch (error) {
      console.error(error);

      // Replace thinking bubble with an error
      setMessages((prev) =>
        prev.map((msg) =>
          msg.id === tempAssistant.id
            ? {
                ...msg,
                content:
                  " Something went wrong. Please try again.",
                loading: false,
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