def is_palindrome_recursive(word, low_index, high_index):
    if word == "":
        return False
    for i in range(high_index // 2):
        if word[low_index] != word[high_index]:
            return False
        low_index += 1
        high_index -= 1
        is_palindrome_recursive(word, low_index, high_index)
        if word[low_index] != word[high_index]:
            return False
    return True


# https://pt.khanacademy.org/computing/computer-science/algorithms/recursive-algorithms/a/using-recursion-to-determine-whether-a-word-is-a-palindrome
# para perder o medo do palíndromo, pesquisei a respeito e encontrei esse
# artigo pesquisei em 27/02/22. Comecei a fazer o requisito, mas tive
# dificuldade para fazer a parte em que ele ia analisando a palavra parte
# por parte, aí depois de assistir um vídeo do Gustavo Guanabara nesselink,
# https://www.youtube.com/watch?v=5VBWe6BXzRo, mas# não consegui implementar,
# e aí tinha esse vídeo como sugestão,
# https://www.youtube.com/watch?v=asNugHKaeRI usei ele para ter a regra de
# negócio de dividir a palavra por 2. Depois de dividir, eu verifico se o
# primeiro e último caracter são iguais, se não, retorna falso, se sim, ele
# incrementa na posição, e decrementa da última, e vai fazendo esse loop pra
# comparar. Ficou faltando verificar se não era um palíndromo, testei algumas
# vezes, e vi que se eu jogasse o que está nas linhas 5 e 6, poderia ir direto
# pra depois de chamar a função, porém era um 'falso positivo', já que as
# linhas 7 e 8, incrementa e decrementa diretamente, se a palavra do teste,
# for diferente de AGUA, dá errado.
# Como "solução" rápida, repeti o código e deu certo.
