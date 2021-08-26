def get_pascal(row):
    current = [1]
    for i in range(row):
        prev = 1
        for j in range(1, i+1):
            tmp = current[j]
            current[j] += prev
            prev = tmp
        current += [1]
    return current
