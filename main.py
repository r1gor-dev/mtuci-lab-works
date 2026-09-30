from calculations import calculation_average, count_positive, find_max

if __name__ == "__main__":
    assert count_positive([-1, 0, 1]) == 1
    assert find_max([-10, -5, -20]) == -5
    assert calculation_average([10, 20, 30]) == 20
    print("Проверки пройдены.")
