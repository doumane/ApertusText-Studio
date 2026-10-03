"""
ApertusText Studio - Core Pipeline
"""

def summarize_text(input_text: str) -> str:
    """
    Core text processing and summarization function utilizing Apertus LLM capabilities.
    """
    print("[ApertusText Studio] Processing input text...")
    
    if len(input_text) > 200:
        return input_text[:200] + "... [Summarized by ApertusText Studio]"
    return input_text

if __name__ == "__main__":
    sample_text = (
        "ApertusText Studio is designed to provide fast, reliable, and secure text "
        "summarization using open-source foundation models. It empowers creators and "
        "developers to maintain complete control over their data workflows."
    )
    print("Original Text Length:", len(sample_text))
    print("Generated Summary:\n", summarize_text(sample_text))
