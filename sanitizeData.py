from string import punctuation # For sanitizing data
def sanitizeData(text):
    """
    Parses a provided text string and attempts to sanitize the provided data by:
    - Replace items in the 'exclude' set with a space
    - convert the text to all lowercase
    - remove one-letter words
    - remove URLs
    
    @param text - string text to sanitize
    @return textClean - sanitized version of provided text
    
    @author Tyler J. Sawyer
    @version 1.0
    """
    text = text.lower()
    
    # Remove HTTP URLs from the text
    text = " ".join([i for i in text.split() if not ("http://" in i) ])
    
    # Set up our exclusions list to remove punctuation from our text.
    exclusions = set(punctuation)
    
    # Filter our set of exclusions from the text.
    textChars = [(" " if char in exclusions else char) for char in text]
    text = "".join(textChars)
    
    # Lastly, remove one-letter words.
    words = text.split()
    goodWords = [word.strip() for word in words if len(word)>1]
    
    return " ".join(goodWords)