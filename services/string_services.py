"""
String Services Module

Provides four string processing services:
- char_count: count total characters
- word_count: count total words
- reverse: reverse the string
- remove_vowels: remove all vowels from the string

Author: Anggota 1
Date: 2024
"""


def char_count(text):
    """
    Count the total number of characters in the given text.
    
    Args:
        text (str): The input string
        
    Returns:
        dict: {
            "status": "success",
            "result": int (number of characters),
            "message": str (human-readable message)
        }
        
    Raises:
        ValueError: If input is not a string or is None
        
    Example:
        >>> char_count("hello")
        {"status": "success", "result": 5, "message": "..."}
    """
    # Validasi input
    if not isinstance(text, str):
        return {
            "status": "error",
            "result": None,
            "message": f"Input must be a string, got {type(text).__name__}"
        }
    
    if text is None:
        return {
            "status": "error",
            "result": None,
            "message": "Input cannot be None"
        }
    
    # Hitung karakter
    count = len(text)
    
    return {
        "status": "success",
        "result": count,
        "message": f"Total {count} character(s) found"
    }


def word_count(text):
    """
    Count the total number of words in the given text.
    
    A word is defined as a sequence of characters separated by whitespace.
    
    Args:
        text (str): The input string
        
    Returns:
        dict: {
            "status": "success",
            "result": int (number of words),
            "message": str (human-readable message)
        }
        
    Raises:
        ValueError: If input is not a string or is None
        
    Example:
        >>> word_count("hello world")
        {"status": "success", "result": 2, "message": "..."}
    """
    # Validasi input
    if not isinstance(text, str):
        return {
            "status": "error",
            "result": None,
            "message": f"Input must be a string, got {type(text).__name__}"
        }
    
    if text is None:
        return {
            "status": "error",
            "result": None,
            "message": "Input cannot be None"
        }
    
    # Hitung kata dengan split()
    words = text.split()
    count = len(words)
    
    return {
        "status": "success",
        "result": count,
        "message": f"Total {count} word(s) found"
    }


