def find_duplicate(nums):
    if not nums:
        return False

    # Metodo para encontrar duplicatas encontrado no site:
    # https://stackoverflow.com/questions/9835762/how-do-i-find-the-duplicates-in-a-list-and-create-another-list-with-them

    isDuplicate = set()

    for num in nums:
        if type(num) is not int or num < 0:
            return False
        if num in isDuplicate:
            return num
        else:
            isDuplicate.add(num)
    return False
