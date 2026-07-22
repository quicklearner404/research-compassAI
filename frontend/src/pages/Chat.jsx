import { useEffect, useState } from "react";
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

  useEffect(() => {
    loadConversation();
  }, [sessionId]);

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

    try {

        await chat(sessionId, text);

    } catch (error) {

        console.error(error);

    }

    const updatedMessages =
        await getMessages(sessionId);

    setMessages(updatedMessages);

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

      <div className="flex-1 overflow-y-auto">
        <MessageList messages={messages} />
      </div>

      <MessageInput onSend={handleSend} />
    </div>
  );
}