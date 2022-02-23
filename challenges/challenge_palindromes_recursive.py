def is_palindrome_recursive(word, low_index, high_index):
    if not word:
        return False

    if not word[low_index] == word[high_index]:
        return False
    # Comments: Se já percorreu metade da string sem ser False, é palíndrome
    elif len(word) // 2 == high_index:
        return True
    else:
        # Source: https://app.betrybe.com/course/computer-science/algoritmo\
        # s/recursividade-e-estrategias-para-solucao-de-problemas/96a4ec77-\
        # 19b6-4dcd-82d2-d7fefb07c74e/conteudos/efb3ba88-ae3a-4386-bb68-8fa\
        # 3677244a4/duas-formas-de-resolver/60acd96c-3cbd-4cdb-8766-6092156\
        # 1738c?use_case=side_bar
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)
