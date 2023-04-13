def sum_nested_list(nested_list):
    summation = 0
    for i in range(len(nested_list)):
        for m in range(len(nested_list[i])):
            summation += nested_list[i][m]
    return summation
