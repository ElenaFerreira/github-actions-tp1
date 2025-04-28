def predict_sentiment(text):
    """
    Predict the sentiment of a given text.

    Args:
        text (str): The input text to analyze.

    Returns:
        str: The predicted sentiment ('positive', 'negative', or 'neutral').
    """
    # Check if the text is empty or None 
    if not text:
        return "neutral"
    
    # Convert the text to lowercase for case-insensitive matching
    lower_text = text.lower()
    
    # Check for positive sentiment keywords
    if "happy" in lower_text or "good" in lower_text:
        return "positive"
    
    # Check for negative sentiment keywords
    if "sad" in lower_text or "bad" in lower_text:
        return "negative"
    
    # Default to neutral if no keywords are matched
    return "neutral"
