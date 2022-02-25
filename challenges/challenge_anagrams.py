def is_anagram(first_string, second_string):
    try:
        if len(first_string) < 2 or len(second_string) < 2:
            return False

        if len(first_string) != len(second_string):
            return False

        first_string = first_string.lower()
        second_string = second_string.lower()

        count = dict()
        for i in first_string:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1

        for i in second_string:
            if not i in count: return False
            if count[i] == 0: return False
            if i in count: 
                count[i] -= 1
            else:
                return False

        return True


    except ValueError:
        return False 
