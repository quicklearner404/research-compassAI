from backend.agent.agent import ResearchAgent

agent = ResearchAgent()

result = agent.run(
    "Find three recent Vision Transformer papers on arXiv."
)

print(result)