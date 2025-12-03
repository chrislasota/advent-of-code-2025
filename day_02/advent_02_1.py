# Advent of Code 2025
# Day 2
# Part 1

def is_invalid_id(id_str):
    size = len(id_str)
    if size % 2 == 1:
        return False
    midpoint = size // 2  # force integer and not a float
    first_half = id_str[:midpoint]
    second_half = id_str[midpoint:]
    return (first_half == second_half)


def main():
    invalid_id_sum = 0
    with open("input_day_02.txt", 'r') as input_file:
        for line in input_file:
            data = line.split(",")
            for str_range in data:
                id_pair = str_range.split("-")
                low_id = int(id_pair[0])
                high_id = int(id_pair[1])
                for id in range(low_id, high_id+1):
                    if is_invalid_id(str(id)):
                        invalid_id_sum += id
    return invalid_id_sum


if __name__ == "__main__":
    print(f"The sum of invalid IDs: {main()}")
