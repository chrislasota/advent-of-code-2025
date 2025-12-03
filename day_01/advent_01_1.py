# Advent of Code 2025
# Day 1 (Dec 1st)
# Part 1

def main():
    combination = 0
    position = 50
    with open("input_day_01.txt", mode="r") as input_file:
        for line in input_file:
            direction = line[0]
            steps = int(line[1:])
            if direction == "R":
                position = (position + steps) % 100
            else:
                position = (position - steps) % 100
            if position == 0:
                combination += 1
    return combination


if __name__ == "__main__":
    print(f"The combination is: {main()}")
