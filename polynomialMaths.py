import numpy as np
import csvMethods

def calculate_delta(a, b, c):
    return b * b - 4 * a * c


def calculate_zero_one(a, b, c, d):
    return (-b - np.sqrt(d)) / (2*a)


def calculate_zero_two(a, b, c, d):
    return (-b + np.sqrt(d)) / (2*a)


def data_dropped_negatives(data_set, col_index):
    rows_to_drop_ids = []
    rows_ids = csvMethods.get_rows_indexes(data_set=data_set)
    for i in rows_ids:
        d = int(data_set.loc[i][col_index])
        if d == 0:
            rows_to_drop_ids.append(i)
    data = data_set.drop(rows_to_drop_ids)
    return data

