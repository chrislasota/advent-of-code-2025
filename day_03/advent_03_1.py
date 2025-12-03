# Advent of Code 2025
# Day 3
# Part 1


def main():
    total_joltage = 0
    with open("input_day_03.txt", 'r') as input_file:
        for line in input_file:
            line = line.rstrip()

            max_left_digit = 0
            max_left_digit_index = 0
            for index in range(len(line) - 1):   # yes, go one less
                digit = int(line[index])
                if digit > max_left_digit:
                    max_left_digit = digit
                    max_left_digit_index = index

            max_right_digit = 0
            for index in range(max_left_digit_index + 1, len(line)):
                digit = int(line[index])
                if digit > max_right_digit:
                    max_right_digit = digit

            total_joltage += (10 * max_left_digit) + max_right_digit

    return total_joltage


if __name__ == "__main__":
    print(f"The total output joltage: {main()}")
