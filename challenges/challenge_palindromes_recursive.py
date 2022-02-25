def is_palindrome_recursive(word, low_index, high_index):
    try:
        if len(word) < 2 and len(word) > 0: return True
        if word[low_index] != word[high_index]: return False
        if low_index >= high_index: return word[low_index] == word[high_index]
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)
    except ValueError:
        return False
    except IndexError:
        return False
