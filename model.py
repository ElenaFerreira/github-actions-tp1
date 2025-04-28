def predict_sentiment(text):
    """
    Predict the sentiment of a given text.
    Args:
        text (str): The input text to analyze.
    Returns:
        str: The predicted sentiment ('positive', 'negative', or 'neutral').
    """
    if not text:
        return "neutral"
    if "happy" in text.lower() or "good" in text.lower():
        return "positive"
    if "sad" in text.lower() or "bad" in text.lower():
        return "negative"
    return "neutral"
