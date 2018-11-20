import random
def main():
    max_columns = 15
    min_columns = 4
    min = 33
    max = 127
    for value in range(min, max + 1):
        print("{:3} {:>4}".format(value, chr(value)))
    columns = int(input("Enter number of columns: "))
    while columns < min_columns or columns > max_columns:
        print("Please use a value between {} and {}".format(min_columns, max_columns))
        columns = int(input("Enter number of columns: "))
    number_of_values = max - min + 1
    rows = number_of_values // columns
    print("Version 1: Horizontal then vertical ordering")
    value = min
    for row in range(rows):
        for column in range(columns):
            print("{:6} {:>2}".format(value, chr(value)), end="")
            value += 1
        print()
    starting_value = value
    for value in range(starting_value, max + 1):
        print("{:6} {:>2}".format(value, chr(value)), end="")
    print("\n")
    print("Version 2: Vertical then horizontal ordering")
    for row in range(rows + 1):
        starting_value = min + row
        value = starting_value
        for column in range(columns - 1):
            value_to_print = value + (column * rows)
            print("{:6} {:>2}".format(value_to_print, chr(value_to_print)), end="")
            value += 1
        value_to_print = value + ((column + 1) * rows)
        if value_to_print <= max:
            print("{:6} {:>2}".format(value_to_print, chr(value_to_print)), end="")
        print()
main()