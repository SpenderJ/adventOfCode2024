from main import calculate_distance
from main import calculate_total_similarity_score


def test_calculate_distance_nominal():
    # Arrange
    list1 = [1, 2, 3, 3, 3, 4]
    list2 = [3, 3, 3, 4, 5, 9]

    # Act
    distance = calculate_distance(list1, list2)

    # Assert
    assert distance == 11


def test_calculate_total_similarity_score_nominal():
    # Arrange
    list1 = [1, 2, 3, 3, 3, 4]
    list2 = [3, 3, 3, 4, 5, 9]

    # Act
    distance = calculate_total_similarity_score(list1, list2)

    # Assert
    assert distance == 31

