FILENAME = "input.txt"


def get_sorted_lists(path: str) -> (list[int], list[int]):
    col1 = []
    col2 = []

    with open(path, 'r') as file:
        for line in file:
            num1, num2 = map(int, line.split())

            col1.append(num1)
            col2.append(num2)

    col1.sort()
    col2.sort()
    return col1, col2


def calculate_distance(list1: list[int], list2: list[int]) -> int:
    distance = 0
    for x in range(len(list1)):
        distance += abs(list1[x] - list2[x])
    return distance


def calculate_total_similarity_score(list1: list[int], list2: list[int]) -> int:
    result = 0
    for x in range(len(list1)):
        result += list1[x] * list2.count(list1[x])
    return result


if __name__ == "__main__":
    list1, list2 = get_sorted_lists(FILENAME)

    # Part 1
    # distance = calculate_distance(list1, list2)

    # Part 2
    distance = calculate_total_similarity_score(list1, list2)

    print(distance)
