def char_count(text):
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


def reverse(text):

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
    
    # Reverse menggunakan slicing
    reversed_text = text[::-1]
    
    return {
        "status": "success",
        "result": reversed_text,
        "message": f"String reversed: '{text}' -> '{reversed_text}'"
    }


def remove_vowels(text):

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
    
    # Vokal yang akan dihapus
    vowels = "aeiouAEIOU"
    
    # Hapus semua vokal
    result = "".join(char for char in text if char not in vowels)
    
    # Hitung vokal yang dihapus
    vowels_removed = len(text) - len(result)
    
    return {
        "status": "success",
        "result": result,
        "message": f"Removed {vowels_removed} vowel(s): '{text}' -> '{result}'"
    }