def char_count(text):
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
        
    count = len(text)    
    return {
        "status": "success",
        "result": count,
        "message": f"Total {count} character(s) found"
    }

def word_count(text):
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
    
    words = text.split()
    count = len(words)    
    return {
        "status": "success",
        "result": count,
        "message": f"Total {count} word(s) found"
    }


def reverse(text):
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

    reversed_text = text[::-1]    
    return {
        "status": "success",
        "result": reversed_text,
        "message": f"String reversed: '{text}' -> '{reversed_text}'"
    }


def remove_vowels(text):
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
    
    vowels = "aeiouAEIOU"
    
    result = "".join(char for char in text if char not in vowels)
    vowels_removed = len(text) - len(result)
    
    return {
        "status": "success",
        "result": result,
        "message": f"Removed {vowels_removed} vowel(s): '{text}' -> '{result}'"
    }