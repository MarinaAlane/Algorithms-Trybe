def is_palindrome_recursive(word, low_index, high_index):
    if not word:
        return False
    if len(word) <= 1:
        return True
    if word[low_index] != word[high_index]:
        return False
    new_word = word[1:high_index]
    new_word_length = len(new_word)
    result = (is_palindrome_recursive(new_word, 0, new_word_length - 1)
              if new_word_length != 0 else True)
    return result
