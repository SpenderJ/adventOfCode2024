import re

FILENAME = "input.txt"


def get_content(path: str) -> str:
    with open(path, 'r') as file:
        file_content = file.read()

    return file_content


def get_summed_operations(file_content: str) -> int:
    pattern = r'(do\(\))|(don\'t\(\))|(mul\((\d+),(\d+)\))'

    enabled = True
    total_sum = 0

    matches = re.findall(pattern, file_content)

    for match in matches:
        if match[0]:  # 'do()' instruction
            enabled = True
        elif match[1]:  # 'don't()' instruction
            enabled = False
        elif match[2]:  # 'mul(X,X)' instruction
            if enabled:
                a, b = int(match[3]), int(match[4])
                total_sum += a * b

    return total_sum


if __name__ == "__main__":
    file_content = get_content(FILENAME)
    print(get_summed_operations(file_content))
