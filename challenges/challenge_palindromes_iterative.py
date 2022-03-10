def is_palindrome_iterative(word):
    if word == '':
        return False

    return word == word[::-1]

# ref: https://github.com/tryber/sd-011-project-algorithms/pull/119/files