import markdown

def format_markdown(text):
    """Formats text into markdown."""
    return markdown.markdown(text)

def clean_text(text):
    """Cleans text by removing unnecessary whitespace."""
    return " ".join(text.split())
# Add other helper functions