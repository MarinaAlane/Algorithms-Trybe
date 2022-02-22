from challenges.utils import sort

def is_anagram(first_string, second_string):
    if sort(first_string) == sort(second_string):
        return True
    else:
        return False
    # checar se a primeira string tem todoas as letras da segunda string na mesma quantidade

    """ Faça o código aqui. """


