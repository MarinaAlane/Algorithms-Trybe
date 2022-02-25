def helper(first_string, second_string):
    first_dict = dict()
    sec_dict = dict()

    for i in range(len(first_string)):
        if  first_string[i] in first_dict:
            first_dict[first_string[i]] += 1
        else:
            first_dict[first_string[i]] = 1

        if second_string[i] in sec_dict:
            sec_dict[second_string[i]] += 1
        else:
            sec_dict[second_string[i]] = 1

    resp = dict()
    resp["first_dict"] = first_dict
    resp["sec_dict"] = sec_dict

    return resp

def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False

    dicts = helper(first_string, second_string)
    first_dict = dicts["first_dict"]
    sec_dict = dicts["sec_dict"]

    for i in range(len(first_string)):
        if first_string[i] not in sec_dict:
            return False
        if(first_dict[first_string[i]] != sec_dict[first_string[i]]):
            return False

    return True
