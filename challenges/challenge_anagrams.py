# def is_anagram(first_string, second_string):
#     if not first_string or not second_string:
#         return False
#     first_list = list()
#     second_list = list()
#     for letters in first_string:
#         first_list.append(letters)
#     for letters in second_string:
#         second_list.append(letters)
#     if so ed(first_list) == so  ed(second_list):
#         return True
#     return False
# -----------------------------------------------------------------------------------------------


# def is_anagram(first_string, second_string):
#     a = int(len(first_string))
#     b = int(len(second_string))
#     if a == b:
#         x = 0
#         if first_string == second_string:
#             return True
#         second_list = list(second_string)
#         for char in first_string:
#             while x < len(second_list):
#                 if second_list[x] == " ":
#                     break
#                 if char == second_list[x]:
#                     print(char, second_list[x], "MARK")
#                     second_list.pop(x)
#                     print("SECOND LIST", second_list)
#                 else:
#                     x+=1
#     return False
# -----------------------------------------------------------------------------------------------

# def is_anagram(first_string, second_string):
#     a = int(len(first_string))
#     b = int(len(second_string))
#     if first_string == second_string:
#         return True
#     if a != b:
#         return False
#     second_list = list(second_string)
#     return 0


# def too_complex(first_string, second_list, b):
#     x = 0
#     for char in first_string:
#         for _ in range(b):
#             if char == second_list[x]:
#                 print(char, second_list[x], "MARK")
#                 second_list.pop(x)
#                 print("SECOND LIST", second_list)
#                 print("VALOR DE X: ", x)
#             x += 1

#     if bool(second_list) == False:
#         return True
#     return False

# -----------------------------------------------------------------------------------------------

# def is_anagram(first_string, second_string, x=0):
#     second_list = list(second_string)
#     i = 0
#     if x == 0:
#         return too_complex(first_string, second_string)
#     for char in first_string:
#         if not bool(second_list):
#             return True
#         for _ in range(len(second_string) + 2):
#             if char == second_string[i]:
#                 second_list.pop(i)
#         i += 1
#     return 0


# def too_complex(first_string, second_string):
#     if len(first_string) != len(second_string):
#         return False
#     if first_string == second_string:
#         return True

#     return is_anagram(first_string, second_string, 1)

# -----------------------------------------------------------------------------------------------

# def is_anagram(first_string, second_string):
#     if len(first_string) != len(second_string):
#         return False
#     if first_string == second_string:
#         return True
#     for char in first_string:
#         for x in enumerate(second_string):
#             if x != char:
#                 return False
#     return True

# -----------------------------------------------------------------------------------------------

# REF: https://stackoverflow.com/questions/8286554/
#       using-python-find-anagrams-for-a-list-of-words/52961395#52961395

def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False
    x = too_complex(first_string)
    y = too_complex(second_string)
    return x == y


def too_complex(string):
    # Creates a dict to count number of times a char appears on a string
    this_dict = {}
    for char in string:
        if char in this_dict:
            this_dict[char] += 1
        else:
            this_dict[char] = 1
    return this_dict
