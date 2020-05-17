def distinctify(positions, numbers):
    for i in range(1, len(positions) - 1):
        if positions[i] == positions[i - 1]:
            del (positions[i])
            del (numbers[i])