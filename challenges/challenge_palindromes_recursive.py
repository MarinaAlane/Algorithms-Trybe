def is_palindrome_recursive(word, low_index, high_index):
    """ Faça o código aqui. """
    if len(word) == 0:
        return False
    elif len(word) == 1 or high_index < low_index:
        return True
    elif word[low_index] == word[high_index]:
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)
    else:
        return False
    

if __name__ == '__main__':
    word = 'AGUA'
    print(is_palindrome_recursive(word, 0, len(word) - 1))
