def sort(array):
    for i in range(len(array)):
        first = i
        for j in range(i + 1, len(array)):
            if (array[j] < array[first]):
                first = j
        array[first], array[i] = array[i], array[first]
    return array

def is_anagram(first_string, second_string):
    try:
        if len(first_string) != len(second_string):
            return False
        list_exist = []
        for i in first_string:
            includ = second_string.find(i)
            if includ != -1:
                list_exist.append(i)
        if (len(list_exist) == len(first_string)
            and sort(list(first_string)) == sort(list(second_string))):
            return True
    except TypeError:
        return False
    return False
    """ Faça o código aqui. """
# https://www.afternerd.com/blog/python-string-contains/
