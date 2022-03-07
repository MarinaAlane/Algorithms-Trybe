def is_anagram(first_string, second_string):
    # Ambas palavras precisam ter o mesmo length
    # sabendo o mesmo length já diminui uma longe de busca
    # precisa verificar se possuem as mesmas letras
    if len(first_string) != len(second_string):
        return False
    
    for value in first_string:
        second_string = second_string.replace(value, '', 1)
    return len(second_string) == 0

# print(is_anagram("pedra", "perdaaa"))
# print(is_anagram(
#         "Lorem ipsum dolor sit amet, consectetur "
#         "adipiscing elit, do sed eiusmod tempor "
#         "incididunt ut labore et dolore magna aliqua.",
        
#         "Lorem ipsum dolor sit amet, consectetur "
#         "adipiscing elit, do sed eiusmod tempor "
#         "incididunt ut labore et dolore magna aliqua."))