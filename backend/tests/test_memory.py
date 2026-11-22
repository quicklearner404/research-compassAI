from backend.services.context import ConversationContext, ConversationMessage
from backend.services.memory import MemoryService
from backend.services.prompt_service import PromptService


def test_empty_history_gives_empty_context():
    context = MemoryService().build_context([])

    assert context.history == []
    assert context.current_query == ""


def test_latest_user_message_becomes_current_query(make_message):
    messages = [
        make_message("user", "What is RAG?"),
        make_message("assistant", "Retrieval augmented generation."),
        make_message("user", "  Find papers on it  "),
    ]

    context = MemoryService(max_recent_messages=3).build_context(messages)

    assert context.current_query == "Find papers on it"
    assert [m.role for m in context.history] == ["user", "assistant"]


def test_history_is_limited_to_recent_window(make_message):
    messages = [make_message("user", f"q{i}") for i in range(10)]

    context = MemoryService(max_recent_messages=3).build_context(messages)

    assert context.current_query == "q9"
    assert [m.content for m in context.history] == ["q7", "q8"]


def test_no_user_message_in_window(make_message):
    messages = [make_message("assistant", "hello")]

    context = MemoryService().build_context(messages)

    assert context.current_query == ""
    assert context.history == []


def test_prompt_includes_history_and_question():
    context = ConversationContext(
        history=[
            ConversationMessage(role="user", content="What is RAG?"),
            ConversationMessage(role="assistant", content="Retrieval augmented generation."),
        ],
        current_query="Find papers on it",
    )

    prompt = PromptService().build(context)

    assert "User:\nWhat is RAG?" in prompt
    assert "Assistant:\nRetrieval augmented generation." in prompt
    assert prompt.rstrip().endswith("## Current User Question\nFind papers on it")


def test_prompt_without_history():
    prompt = PromptService().build(ConversationContext(history=[], current_query="hi"))

    assert "No previous conversation." in prompt
