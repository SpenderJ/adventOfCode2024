import pytest

from main import check_line_safe, check_line_removing_an_element


@pytest.mark.parametrize("line, is_safe", [
    ([7, 6, 4, 2, 1], True),   # Safe line
    ([1, 2, 7, 8, 9], False),  # Not safe line
    ([9, 7, 6, 2, 1], False),   # Not safe line
    ([1, 3, 2, 4, 5], False),  # Not safe line
    ([8, 6, 4, 4, 1], False),   # Not safe line
    ([1, 3, 6, 7, 9], True),  # Safe line
])
def test_check_line_safe_nominal(line: list[int], is_safe: bool):
    # Act
    result = check_line_safe(line)

    # Assert
    assert result == is_safe


@pytest.mark.parametrize("line, is_safe", [
    ([7, 6, 4, 2, 1], True),   # Safe line
    ([1, 2, 7, 8, 9], False),  # Not safe line
    ([9, 7, 6, 2, 1], False),   # Not safe line
    ([1, 3, 2, 4, 5], True),  # Safe line
    ([8, 6, 4, 4, 1], True),   # Safe line
    ([1, 3, 6, 7, 9], True),  # Safe line
])
def test_check_line_safe_part_2(line: list[int], is_safe: bool):
    # Act
    result = False
    if check_line_safe(line):
        result = True
    elif check_line_removing_an_element(line):
        result = True

    # Assert
    assert result == is_safe
