# Expansions for ambiguous one-word queries, shared by search tools.
QUERY_ENRICHMENTS = {
    "transformer": '"transformer" machine learning',
    "transformers": '"transformer" machine learning',
    "cnn": '"convolutional neural network" deep learning',
    "bert": '"bert" natural language processing',
    "gpt": '"gpt" large language model',
    "llm": '"large language model"',
    "vit": '"vision transformer"',
    "clip": '"clip" vision language model',
    "gan": '"generative adversarial network"',
    "diffusion": '"diffusion model"',
    "rag": '"retrieval augmented generation"',
}


def enrich_query(query: str) -> str:
    """Expand a single ambiguous keyword (e.g. "rag") into a precise query."""
    normalized = query.lower().strip()
    if len(normalized.split()) == 1:
        return QUERY_ENRICHMENTS.get(normalized, query)
    return query
