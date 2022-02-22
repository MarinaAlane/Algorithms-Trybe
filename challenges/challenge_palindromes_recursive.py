def is_palindrome_recursive(word, low_index, high_index):
    if word == '':
        return False
    elif len(word) == 1:
        return True
    elif len(word) <= 2 and word[low_index] == word[high_index]:
        return True
    elif len(word) <= 2 and word[low_index] != word[high_index]:
        return False
    else:
        wrd = word[low_index+1:len(word)-1]
        return is_palindrome_recursive(wrd, low_index, len(wrd)-1)
