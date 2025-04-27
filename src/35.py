def is_palindrome(word):
    """
    Check if a given word is a palindrome.
    
    A palindrome is a word that reads the same backward as forward.
    """
    # Convert the word to lowercase and remove non-alphanumeric characters
    cleaned_word = ''.join(c.lower() for c in word if c.isalnum())
    # Compare the cleaned word with its reverse
    return cleaned_word == cleaned_word[::-1]

# Example usage:
print(is_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_palindrome("Hello, World!"))  # False
