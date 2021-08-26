def generate_pascal_triangle(num_of_rows: int) -> List[List[int]]:
    output = [[1]]
    for i in range(num_of_rows - 1):
        l = [1] * (i + 2)
        for j in range(i + 2):
            if 0 < j < i + 1:
                l[j] = output[i][j - 1] + output[i][j]
        output.append(list(l))
    return output


def other_pascal(num_of_rows: int) -> List[List[int]]:
    output = [[1]]
    for _ in range(num_of_rows-1):
        output.append(list(map(lambda x, y: x + y, output[-1] + [0], [0] + output[-1])))
    return output
