def is_anagram(first_string, second_string):
    if not first_string or not second_string:
        return False
    
    found=0

    for i in range(len(first_string)):
        found = 0
        for j in range(len(first_string)):
            if first_string[i] == second_string[j]:
                found = 1
                break
        if found==0:
            return False
    else:
        return True
