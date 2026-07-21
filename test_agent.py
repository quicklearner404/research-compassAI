from agent.agent import ResearchAgent

agent = ResearchAgent()

response = agent.run(
    "I want to learn Graph Neural Networks from scratch. Give me the best papers, GitHub repositories, and tutorials."
)

print("\n" + "=" * 80)
print(response)
print("=" * 80)