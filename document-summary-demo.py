"""
Document Summary Demo

This is a simple Python demo that creates a basic structured summary
from a block of text.

It does not use an LLM.
It demonstrates the type of summarization workflow often used before
integrating an AI model.

This demo is for learning and portfolio purposes only.
"""

from typing import List


SAMPLE_DOCUMENT = """
Artificial intelligence is becoming an important part of modern business.
Organizations are using AI to improve customer support, automate repetitive
work, summarize documents, analyze data, and support decision-making.

However, AI adoption also creates risks. These risks include incorrect outputs,
data privacy concerns, lack of transparency, over-reliance on AI systems, and
unclear accountability.

A responsible AI approach should include governance, human review, monitoring,
security controls, and clear business ownership. AI should be used to support
people, not remove human judgment from high-risk decisions.

For enterprise adoption, organizations should start with clear business use
cases, validate value through MVPs, and scale only after testing reliability,
user adoption, data readiness, and governance controls.
"""


def split_into_sentences(text: str) -> List[str]:
    """
    Split text into simple sentences.

    This is a basic example. Production systems may use NLP libraries
    or LLMs for better sentence detection.
    """
    cleaned_text = " ".join(text.strip().split())
    raw_sentences = cleaned_text.split(".")

    sentences = [
        sentence.strip()
        for sentence in raw_sentences
        if sentence.strip()
    ]

    return sentences


def summarize_text(text: str, max_sentences: int = 3) -> str:
    """
    Create a simple extractive summary by selecting the first few sentences.

    This is not advanced AI summarization. It is a simple demonstration
    of how text can be converted into a shorter summary.
    """
    sentences = split_into_sentences(text)

    if not sentences:
        return "No valid text found for summarization."

    selected_sentences = sentences[:max_sentences]
    summary = ". ".join(selected_sentences) + "."

    return summary


def extract_key_points(text: str) -> List[str]:
    """
    Extract simple key points using keyword checks.
    """
    sentences = split_into_sentences(text)
    key_points = []

    important_keywords = [
        "AI",
        "risks",
        "governance",
        "human review",
        "enterprise",
        "MVP",
        "security",
        "accountability",
    ]

    for sentence in sentences:
        sentence_lower = sentence.lower()
        for keyword in important_keywords:
            if keyword.lower() in sentence_lower:
                key_points.append(sentence)
                break

    return key_points[:5]


def run_demo() -> None:
    """
    Run the document summary demo.
    """
    print("Document Summary Demo")
    print("----------------------")
    print("\nOriginal Document:")
    print(SAMPLE_DOCUMENT.strip())

    summary = summarize_text(SAMPLE_DOCUMENT, max_sentences=3)
    key_points = extract_key_points(SAMPLE_DOCUMENT)

    print("\nShort Summary:")
    print(summary)

    print("\nKey Points:")
    for index, point in enumerate(key_points, start=1):
        print(f"{index}. {point}.")

    print("\nGovernance Note:")
    print(
        "For high-risk documents, AI-generated summaries should be reviewed "
        "by a qualified human before use."
    )


if __name__ == "__main__":
    run_demo()
