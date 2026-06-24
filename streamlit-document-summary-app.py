"""
Streamlit Document Summary Demo

A simple Streamlit app that demonstrates document summarization logic
without using a real LLM.

This is a public portfolio demo showing how an AI document workflow
could be structured safely before adding a production AI model.

Run locally:
    streamlit run streamlit-document-summary-app.py
"""

from typing import List
import streamlit as st


def split_into_sentences(text: str) -> List[str]:
    """
    Split text into simple sentences.
    This is a basic demo method, not production NLP.
    """
    cleaned_text = " ".join(text.strip().split())
    raw_sentences = cleaned_text.split(".")

    return [sentence.strip() for sentence in raw_sentences if sentence.strip()]


def summarize_text(text: str, max_sentences: int = 3) -> str:
    """
    Create a simple extractive summary using the first few sentences.
    """
    sentences = split_into_sentences(text)

    if not sentences:
        return "No valid text found for summarization."

    selected_sentences = sentences[:max_sentences]
    return ". ".join(selected_sentences) + "."


def extract_key_points(text: str) -> List[str]:
    """
    Extract simple key points using keyword checks.
    """
    sentences = split_into_sentences(text)

    important_keywords = [
        "AI",
        "risk",
        "governance",
        "human review",
        "enterprise",
        "MVP",
        "security",
        "accountability",
        "data",
        "compliance",
    ]

    key_points = []

    for sentence in sentences:
        sentence_lower = sentence.lower()
        for keyword in important_keywords:
            if keyword.lower() in sentence_lower:
                key_points.append(sentence)
                break

    return key_points[:5]


def classify_risk(text: str) -> str:
    """
    Simple keyword-based risk classification.
    """
    high_risk_keywords = [
        "legal",
        "financial",
        "compliance",
        "personal data",
        "contract",
        "medical",
        "employment",
    ]

    text_lower = text.lower()

    for keyword in high_risk_keywords:
        if keyword in text_lower:
            return "High review recommended"

    return "Standard review"


def main() -> None:
    st.set_page_config(
        page_title="AI Document Summary Demo",
        page_icon="🤖",
        layout="centered",
    )

    st.title("AI Document Summary Demo")
    st.write(
        "A simple public demo showing how document summarization, key point extraction, "
        "and review classification can be structured before adding a production AI model."
    )

    st.info(
        "This demo does not use a real LLM. It uses simple Python logic for educational "
        "and portfolio purposes."
    )

    sample_text = """
Artificial intelligence is becoming an important part of modern business.
Organizations are using AI to improve customer support, automate repetitive work,
summarize documents, analyze data, and support decision-making.

However, AI adoption also creates risks. These risks include incorrect outputs,
data privacy concerns, lack of transparency, over-reliance on AI systems, and unclear accountability.

A responsible AI approach should include governance, human review, monitoring,
security controls, and clear business ownership. AI should be used to support people,
not remove human judgment from high-risk decisions.
"""

    user_text = st.text_area(
        "Paste document text here",
        value=sample_text.strip(),
        height=250,
    )

    max_sentences = st.slider(
        "Summary length",
        min_value=1,
        max_value=5,
        value=3,
    )

    if st.button("Generate Summary"):
        summary = summarize_text(user_text, max_sentences=max_sentences)
        key_points = extract_key_points(user_text)
        risk_level = classify_risk(user_text)

        st.subheader("Short Summary")
        st.write(summary)

        st.subheader("Key Points")
        if key_points:
            for index, point in enumerate(key_points, start=1):
                st.write(f"{index}. {point}.")
        else:
            st.write("No key points detected using the current demo logic.")

        st.subheader("Review Classification")
        st.write(risk_level)

        st.warning(
            "Governance note: For high-risk documents, summaries and recommendations "
            "should be reviewed by a qualified human before use."
        )


if __name__ == "__main__":
    main()
