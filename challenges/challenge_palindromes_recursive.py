# https://www.youtube.com/watch?v=92UyahoAne4
def is_palindrome_recursive(word, low_index, high_index):
    # base case
    if not word or word[low_index] != word[high_index]:
        return False
    if len(word) == 1 or low_index >= high_index:
        return True
    else:
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)
