import MessageBubble from "./MessageBubble";

export default function MessageList({ messages }) {
  const messageList = Array.isArray(messages) ? messages : [];

  return (
    <div className="flex flex-col gap-4 p-8">
      {messageList.map((message) => (
        <MessageBubble
          key={message.id || `${message.role}-${message.content}`}
          role={message.role}
          content={message.content}
        />
      ))}
    </div>
  );
}