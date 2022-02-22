def get_list(list):
    create_list = {}
    for i in list:
        if i in create_list: 
            return i
        if type(i) is not int or i < 0:
            return False
        else:
            create_list[i] = 1
    return False

def find_duplicate(nums):
    create_list = get_list(nums)

    if create_list is None:
        return False
    else:
        return create_list

