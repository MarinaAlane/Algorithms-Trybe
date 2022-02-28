def is_palindrome_recursive(word, low_index, high_index):
    if not word or word[low_index] != word[high_index]:
        return False
# Teste 1 sem palavra ou final diferente do começo
    if len(word) == 1 or low_index >= high_index:
        return True
# Teste 2 palavra com 1 letra ou maior que 1
    else:
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)