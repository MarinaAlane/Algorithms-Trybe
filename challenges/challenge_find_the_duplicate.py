from challenges.challenge_anagrams import merge_sort


def find_duplicate(nums):
    try:
        validate_input(nums)
        sorted = merge_sort(nums)
        for i in range(1, len(sorted)):
            current = sorted[i]
            previous = sorted[i - 1]
            if (current == previous):
                return current

        return False
    except ValueError:
        return False


def validate_input(nums):
    if not nums:
        raise ValueError()

    for entry in nums:
        if type(entry) is not int:
            raise ValueError()

        if entry < 0:
            raise ValueError()
