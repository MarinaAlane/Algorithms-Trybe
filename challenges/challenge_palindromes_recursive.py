def is_palindrome_recursive(word, low_index, high_index):
    if len(word) <= 2:
        return True
    else:
        if word[low_index] == word[high_index]:
            n_arr = word[low_index+1:high_index-1]
            is_palindrome_recursive(n_arr, low_index, len(n_arr))
    # base case: check if word length is smaller or equals two?
    # check if word low index === word high index
    # if true for both, return true
    # if true only for second, cut the words low and high index and call func again

    """ Faça o código aqui. """
