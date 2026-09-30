def calculation_average(numbers):
    if not numbers:
        raise ValueError("Список пуст")
    total_sum = 0
    num_length = len(numbers)
    for num in numbers:
        total_sum = total_sum + num
    expression = total_sum / num_length
    return expression


def find_max(numbers):
    max_value = numbers[0]
    for num in numbers:
        max_value = max(max_value, num)
    return max_value


def count_positive(numbers):
    count = 0
    for num in numbers:
        if num > 0:
            count += 1
    return count


def analyze_data(numbers):
    if not numbers:
        raise ValueError("Список пуст.")

    total_sum = 0
    max_value = numbers[0]
    min_value = numbers[0]

    for num in numbers:
        total_sum += num
        max_value = max(max_value, num)
        min_value = min(min_value, num)
    return min_value, max_value, total_sum / len(numbers)
