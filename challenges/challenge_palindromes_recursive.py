def is_palindrome_recursive(word, low_index, high_index):
    try:
        if (low_index - high_index) < 2: 
            if word[low_index] == word[high_index]:
                return is_palindrome_recursive(word, low_index+1, high_index-1)
            else:
                return False
        return True
    except TypeError:
        return False
    except IndexError:
        return False
