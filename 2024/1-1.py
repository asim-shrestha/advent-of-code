from typing import Tuple


def main(list1: list[int], list2: list[int]):
    # Sort left and right list
    list1.sort()
    list2.sort()

    # Iterate through a zip and get diffs
    diffs = [abs(a - b) for a, b in zip(list1, list2)]

    total_sum = sum(diffs)
    print("Part 1:", total_sum)

    keys = set(list1 + list2)
    right_list_count = {
        key: list2.count(key)
        for key in keys
    }

    similarity_scores = [
        value * right_list_count[value]
        for value in list1
    ]

    print("Part 2:", sum(similarity_scores))


if __name__ == "__main__":
    with open("./2024/1-input.txt", "r") as file:
        lines = file.readlines()
        delimiter = "   "
        data: list[Tuple[int, int]] = [(int(string.split(delimiter)[0]), int(string.split(delimiter)[1])) for string in lines]
        list1 = [pair[0] for pair in data]
        list2 = [pair[1] for pair in data]

    main(list1, list2)
