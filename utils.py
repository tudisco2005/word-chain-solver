import typing

def is_valid_connection(word1: str, word2: str) -> bool:
    """
    Returns True if the two words are connected by a single letter difference.
    """
    if len(word1) != len(word2):
        return False

    diff_count = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            diff_count += 1
        if diff_count > 1:
            return False

    return diff_count == 1