def order(word):
    abc = {}
    for letter in word:
        if letter in abc:
            abc[letter] += 1
        else:
            abc[letter] = 1
    return abc

def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False
    first_string = order(first_string)
    second_string = order(second_string)    
    
    if first_string == second_string:
        return True
    else:
        return False
