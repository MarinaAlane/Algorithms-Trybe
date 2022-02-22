def custom_reverce(word, low_index, high_index):
    if low_index == high_index:
        return word
    return (
        custom_reverce(word[1:], low_index, len(word[1:]) - 1)
        + word[0]
    )
