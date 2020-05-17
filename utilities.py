import re

def distinctify(positions, numbers):
    if len(positions)<=1:
        return
    for i in range(1, len(positions) - 1):
        if positions[i] == positions[i - 1]:
            del (positions[i])
            del (numbers[i])


def parse_string_regex(string):
    regex_pos = re.compile(r'tile-position-\d-\d')
    regex_nums = re.compile(r'"tile-inner">\d')
    positions = [pos[-4:].replace('-', '') for pos in regex_pos.findall(string)]
    numbers = [num[-1] for num in regex_nums.findall(string)]

    return positions, numbers
