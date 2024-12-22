from main import get_summed_operations


def test_get_summed_operations_nominal():
    # Arrange
    file_content = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

    # Act
    result = get_summed_operations(file_content)

    # Assert
    assert result == 161


def test_get_summed_operations_with_dos_nominal():
    # Arrange
    file_content = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

    # Act
    result = get_summed_operations(file_content)

    # Assert
    assert result == 48
