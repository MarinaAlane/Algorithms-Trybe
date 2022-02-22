def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False
    if not validate_anagram(first_string, second_string):
        return False
    else:
        return True

# Basicamente ele vai comparando a primeira letra da second_string
# com todas as letras do first_string caso ele encontre ele passa pra segunda
# letra e assim vai, se não encontrar alguma das letras ele retorna falso


def validate_anagram(first_string, second_string):
    first_list = list(first_string)
    second_list = list(second_string)
    first_count = 0
    second_count = 0
    while True:
        if len(first_list) == first_count:
            return False
        if first_list[first_count] == second_list[second_count]:
            del(first_list[first_count])
            del(second_list[second_count])
            first_count = 0
            second_count = 0
        else:
            first_count += 1
        if len(first_list) == 0:
            break
    return True
