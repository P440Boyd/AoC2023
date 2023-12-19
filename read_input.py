def read_input_from_daynum(day_number, readlines=True):
    if readlines:
        with open(f"Solutions/Day_{day_number}/input.txt", "r") as input_fp:
            input_lines = input_fp.readlines()
            return [line.strip() for line in input_lines]
    with open(f"Day_{day_number}/input.txt", "r") as input_fp:
        return input_fp.read()
