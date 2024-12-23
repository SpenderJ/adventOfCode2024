import itertools

FILENAME = "input.txt"


def get_array(path: str) -> list[str]:
    array = []

    with open(path, 'r') as file:
        for line in file:
            array.append(line.strip('\n'))
    return array


def get_variations_from_word(word: str) -> list[str]:
    array = [word, word[::-1]]
    return array


def explore_map_to_find_XMAS(map: list[str]) -> int:
    total_count = 0
    rows = len(map)
    cols = len(map[0])

    def matches_x_pattern(r: int, c: int):
        forward = (map[r-1][c-1] == 'M' and map[r][c] == 'A' and map[r+1][c+1] == 'S')
        backward = (map[r-1][c-1] == 'S' and map[r][c] == 'A' and map[r+1][c+1] == 'M')
        reverse_forward = (map[r-1][c+1] == 'S' and map[r][c] == 'A' and map[r+1][c-1] == 'M')
        reverse_backward = (map[r-1][c+1] == 'M' and map[r][c] == 'A' and map[r+1][c-1] == 'S')

        return (forward or backward) and (reverse_forward or reverse_backward)

    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            if matches_x_pattern(r, c):
                total_count += 1

    return total_count


def explore_map_to_find_word(map: list[str], word_array: list[str]):
    total_count = 0

    for row in map:
        for word in word_array:
            total_count += row.count(word)

    num_columns = len(map[0])
    for col in range(num_columns):
        column_str = ''.join(map[row][col] for row in range(len(map)))
        for word in word_array:
            total_count += column_str.count(word)

    for start_row in range(len(map)):
        diagonal_str = ''.join(map[start_row + i][i] for i in range(min(len(map) - start_row, num_columns)))
        for word in word_array:
            total_count += diagonal_str.count(word)

    for start_col in range(1, num_columns):
        diagonal_str = ''.join(map[i][start_col + i] for i in range(min(len(map), num_columns - start_col)))
        for word in word_array:
            total_count += diagonal_str.count(word)

    for start_row in range(len(map)):
        diagonal_str = ''.join(
            map[start_row + i][num_columns - 1 - i] for i in range(min(len(map) - start_row, num_columns)))
        for word in word_array:
            total_count += diagonal_str.count(word)

    for start_col in range(1, num_columns):
        diagonal_str = ''.join(
            map[i][num_columns - 1 - start_col - i] for i in range(min(len(map), num_columns - start_col)))
        for word in word_array:
            total_count += diagonal_str.count(word)

    return total_count


if __name__ == "__main__":
    word = "XMAS"
    map = get_array(FILENAME)
    word_array = get_variations_from_word(word)
    print(explore_map_to_find_word(map, word_array))
    print(explore_map_to_find_XMAS(map))

