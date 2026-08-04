from backend.agent.agent import should_use_direct_response


def test_simple_greeting_uses_direct_response():
    assert should_use_direct_response("hello") is True
    assert should_use_direct_response("hi there") is True


def test_research_request_does_not_use_direct_response():
    assert should_use_direct_response("find recent papers about transformers") is False
    assert should_use_direct_response("search github for llm repos") is False
