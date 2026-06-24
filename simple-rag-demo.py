"""
Simple RAG Demo

This is a beginner-friendly Retrieval-Augmented Generation style demo.

It does not use a real LLM or vector database.
Instead, it demonstrates the basic RAG flow:

1. User asks a question
2. System retrieves relevant context from a small knowledge base
3. System generates a simple response using the retrieved context

This demo is for learning and portfolio purposes only.
"""

from typing import List, Dict


KNOWLEDGE_BASE: List[Dict[str, str]] = [
    {
        "title": "What is RAG?",
        "content": (
            "Retrieval-Augmented Generation, or RAG, is an AI pattern where "
            "a system retrieves relevant information from trusted sources before "
            "generating an answer. It helps reduce hallucination and improves "
            "answer grounding."
        ),
    },
    {
        "title": "Why enterprises use RAG",
        "content": (
            "Enterprises use RAG to connect AI assistants with internal documents, "
            "policies, knowledge bases, product manuals, compliance documents, and "
            "business data. This helps users get answers based on approved information."
        ),
    },
    {
        "title": "RAG governance",
        "content": (
            "RAG systems should include access control, source tracking, logging, "
            "monitoring, human review for high-risk responses, and regular knowledge "
            "base updates."
        ),
    },
    {
        "title": "Human-in-the-loop",
        "content": (
            "Human-in-the-loop means that AI can assist with analysis or drafting, "
            "but a human reviews, approves, edits, or rejects the output before final use."
        ),
    },
]


def score_document(query: str, document: Dict[str, str]) -> int:
    """
    Very simple keyword matching score.

    A production RAG system would normally use embeddings,
    vector search, hybrid search, or semantic retrieval.
    """
    query_words = set(query.lower().split())
    content_words = set(document["content"].lower().split())
    title_words = set(document["title"].lower().split())

    return len(query_words.intersection(content_words)) + len(query_words.intersection(title_words))


def retrieve_context(query: str, top_k: int = 2) -> List[Dict[str, str]]:
    """
    Retrieve the most relevant documents from the knowledge base.
    """
    scored_documents = [
        {
            "title": document["title"],
            "content": document["content"],
            "score": score_document(query, document),
        }
        for document in KNOWLEDGE_BASE
    ]

    ranked_documents = sorted(
        scored_documents,
        key=lambda item: item["score"],
        reverse=True,
    )

    return [doc for doc in ranked_documents[:top_k] if doc["score"] > 0]


def generate_answer(query: str, retrieved_docs: List[Dict[str, str]]) -> str:
    """
    Generate a simple answer using retrieved context.

    In a real implementation, this step would call an LLM and pass
    the retrieved context into the prompt.
    """
    if not retrieved_docs:
        return (
            "I could not find enough relevant information in the knowledge base. "
            "Please add more trusted source content or refine the question."
        )

    context = "\n\n".join(
        f"Source: {doc['title']}\n{doc['content']}"
        for doc in retrieved_docs
    )

    answer = (
        f"Question: {query}\n\n"
        "Answer based on retrieved context:\n"
        f"{context}\n\n"
        "Summary:\n"
        "The response above is grounded in the retrieved knowledge base content. "
        "For high-risk use cases, a human reviewer should validate the answer before use."
    )

    return answer


def run_demo() -> None:
    """
    Run the simple RAG demo.
    """
    print("Simple RAG Demo")
    print("----------------")
    print("Example questions:")
    print("- What is RAG?")
    print("- Why do enterprises use RAG?")
    print("- How should RAG be governed?")
    print("- What is human-in-the-loop?")
    print()

    query = input("Enter your question: ").strip()

    if not query:
        print("No question entered. Please run again and enter a question.")
        return

    retrieved_docs = retrieve_context(query)
    answer = generate_answer(query, retrieved_docs)

    print("\nRetrieved Documents:")
    for doc in retrieved_docs:
        print(f"- {doc['title']} (score: {doc['score']})")

    print("\nGenerated Response:")
    print(answer)


if __name__ == "__main__":
    run_demo()
