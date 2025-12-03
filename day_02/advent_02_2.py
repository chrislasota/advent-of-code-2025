# Advent of Code 2025
# Day 2
# Part 2

def is_invalid_id(id_str):
    # We first double the input string, and then run a count
    # of how many times the original input string matches
    # a same-width substring of the doubled string.  If that
    # number of times is more than 2 (at start/end), then
    # we have an invalid number.
    size = len(id_str)
    double_id_str = id_str + id_str
    match_count = 0
    for i in range(2*size):
        if double_id_str[i:i+size] == id_str:
            match_count +=1
    return (match_count > 2)


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
