def get_schema(list):
    schema = dict()

    for item in list:
        if type(item) is not int or item < 0:
            return False

        schema[item] = schema.get(item, 0) + 1

    return schema


def find_duplicate(nums):
    schema = get_schema(nums)

    if not schema:
        return False

    duplicate = False

    for attribute, value in schema.items():
        if value > 1:
            duplicate = attribute

    return duplicate
