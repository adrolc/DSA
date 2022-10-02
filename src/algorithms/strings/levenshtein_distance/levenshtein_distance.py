"""
Implementation of the levenshtein distance.
Levenshtein distance is a string metric for measuring the difference between two sequences
"""


def levenshtein_distance(sequence1: str, sequence2: str) -> int:
    # Longer sequence should come first
    if len(sequence1) > len(sequence2):
        sequence1, sequence2 = sequence2, sequence1

    prev_row = list(range(len(sequence1) + 1))
    for row, char_s2 in enumerate(sequence2):
        current_row = [row + 1]
        for col, char_s1 in enumerate(sequence1):
            if char_s1 == char_s2:
                current_row.append(prev_row[col])
            else:
                current_row.append(
                    1
                    + min(
                        prev_row[col],  # replace
                        prev_row[col + 1],  # insert
                        current_row[-1],  # remove
                    )
                )
        prev_row = current_row
    return prev_row[-1]
