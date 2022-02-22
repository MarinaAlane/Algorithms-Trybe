def custom_reverse(word, low_index, high_index):
    if low_index == high_index:
        return word
    return (
        custom_reverse(word[1:], low_index, len(word[1:]) - 1)
        + word[0]
    )
