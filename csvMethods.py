import pandas as pd


def import_data(filename, separator, names, incorrect_data, rows_to_skip):
    data_frame = pd.read_csv(filename, sep=separator, names=names, na_values=incorrect_data, skiprows=rows_to_skip)
    clean_data = data_frame.dropna()
    return clean_data


def save_output(data, filename, separator):
    return data.to_csv(filename, sep=separator)


def get_rows_indexes(data_set):
    return [row[0] for row in data_set.iterrows()]


def add_column(row_index, column_name, data_set, value):
    if column_name not in data_set:
        data_set.insert(loc=row_index, column=column_name, value=value)
    return



