def is_palindrome_recursive(word, low_index, high_index):
    try:
        if low_index >= (len(word) // 2) - 1:
            return word[low_index] == word[high_index]
        return (word[low_index] == word[high_index]
            and is_palindrome_recursive(word, low_index + 1, high_index - 1))
    except ValueError:
        return False
    except IndexError:
        return False
