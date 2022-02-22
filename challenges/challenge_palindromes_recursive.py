def is_palindrome_recursive(word, low_index, high_index):
    if not word:
        return False
    # verificando a parte central da palavra
    # palavras em numero impar
    if low_index >= high_index:
        return True
    if word[low_index] == word[high_index]:
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)
    return False


if __name__ == "__main__":
    print(is_palindrome_recursive("ANA", 0, 2))
    print(is_palindrome_recursive("COXINHA", 0, 6))
    print(is_palindrome_recursive("REVIVER", 0, 6))


# usando recursividade - palindromo
# https://pt.khanacademy.org/computing/computer-science/algorithms/recursive-algorithms/a/using-recursion-to-determine-whether-a-word-is-a-palindrome#:~:text=Ent%C3%A3o%2C%20%C3%A9%20assim%20que%20podemos,o%20subproblema%20%E2%80%94%20%C3%A9%20um%20pal%C3%ADndromo.
# https://machadodev.github.io/Recursion/
# https://www.youtube.com/watch?v=asNugHKaeRI
