def is_palindrome_recursive(word, low_index, high_index):
    if word == "":
        return False

    if word[low_index] != word[high_index]:
        return False

    if low_index >= high_index and len(word) > 0:
        return True

    return is_palindrome_recursive(word, low_index + 1, high_index - 1)

# Recebi ajuda do Luciano Pimenta para a resolução deste requisito.