FILENAME = "input.txt"


def get_array(path: str) -> (list[int], list[int]):
    array = []

    with open(path, 'r') as file:
        for line in file:
            array.append(list(map(int, line.split())))

    return array


def check_line_safe(line: list[int]) -> bool:
    if sorted(line) != line and sorted(line, reverse=True) != line:  # Check that the line is well in the same order
        return False
    for y in range(1, len(line)):
        diff = line[y - 1] - line[y]
        if abs(diff) < 1 or abs(diff) > 3:  # Check that the diff is well between 1 and 3
            return False
    return True


def check_line_removing_an_element(line: list[int]) -> bool:
    for y in range(len(line)):
        line_updated = line[:y] + line[y + 1:]

        if check_line_safe(line_updated):
            return True
    return False


if __name__ == "__main__":
    array = get_array(FILENAME)
    number_of_true = 0
    for line in array:
        if check_line_safe(line):
            number_of_true += 1
        elif check_line_removing_an_element(line):
            number_of_true += 1

    print(number_of_true)
