def read_matrix(rows, cols, data_type=int):
    matrix = []
    for _ in range(rows):
        row = []
        for _ in range(cols):
            row.append(data_type(input()))
        matrix.append(row)
    return matrix


rows, cols = map(int, input().split())

type_map = {"int": int, "float": float, "bool": bool}

data_type = type_map[input()]

matrix = read_matrix(rows, cols, data_type)

print(matrix)
