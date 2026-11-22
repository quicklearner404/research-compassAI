"""
Run the research agent once from the command line, without the web UI.

Usage (from the project root):
    python -m scripts.run_agent "Find three recent Vision Transformer papers on arXiv"
    USE_MOCK_LLM=true python -m scripts.run_agent "hello"   # no API keys needed
"""

import argparse

from backend.agent.agent import ResearchAgent, needs_tools


def main() -> None:
    parser = argparse.ArgumentParser(description="Ask Research Compass AI a question.")
    parser.add_argument("query", help="Question or research request")
    args = parser.parse_args()

    route = "tool-calling agent" if needs_tools(args.query) else "direct LLM"
    print(f"[route] {route}\n")

    print(ResearchAgent().run(args.query))


if __name__ == "__main__":
    main()
