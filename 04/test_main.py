from main import explore_map_to_find_word, get_variations_from_word, explore_map_to_find_XMAS


def test_explore_map_to_find_word_nominal():
    # Arrange
    map = [
        "MMMSXXMASM",
        "MSAMXMSMSA",
        "AMXSXMAAMM",
        "MSAMASMSMX",
        "XMASAMXAMM",
        "XXAMMXXAMA",
        "SMSMSASXSS",
        "SAXAMASAAA",
        "MAMMMXMMMM",
        "MXMXAXMASX",
    ]
    word_array = get_variations_from_word("XMAS")

    # Act

    result = explore_map_to_find_word(map, word_array)

    # Assert
    assert result == 18


def test_explore_map_to_find_XMAS_nominal():
    # Arrange
    map = [
        "MMMSXXMASM",
        "MSAMXMSMSA",
        "AMXSXMAAMM",
        "MSAMASMSMX",
        "XMASAMXAMM",
        "XXAMMXXAMA",
        "SMSMSASXSS",
        "SAXAMASAAA",
        "MAMMMXMMMM",
        "MXMXAXMASX",
    ]

    # Act

    result = explore_map_to_find_XMAS(map)

    # Assert
    assert result == 9
