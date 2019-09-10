import csvMethods
import polynomialMaths

incorrectData = ['foo', 'bar']
data_frame = csvMethods.import_data(
    filename='polynomial.csv',
    separator=';',
    names=['A', 'B', 'C'],
    incorrect_data=incorrectData,
    rows_to_skip=1)


def add_delta_col():
    rows_ids = csvMethods.get_rows_indexes(data_set=data_frame)
    delta = []
    for i in rows_ids:
        a = data_frame.loc[i][0]
        b = data_frame.loc[i][1]
        c = data_frame.loc[i][2]
        value = polynomialMaths.calculate_delta(a, b, c)
        delta.append(value)
    csvMethods.add_column(row_index=3, column_name='\u0394', data_set=data_frame, value=delta)
    return


def calculate_zeros(data_set):
    rows_ids = csvMethods.get_rows_indexes(data_set)
    zero_one = []
    zero_two = []
    for i in rows_ids:
        a = data_set.loc[i][0]
        b = data_set.loc[i][1]
        c = data_set.loc[i][2]
        d = data_set.loc[i][3]
        zero_one.append(polynomialMaths.calculate_zero_one(a, b, c, d))
        zero_two.append(polynomialMaths.calculate_zero_two(a, b, c, d))
    csvMethods.add_column(row_index=4, column_name='$x_1$', data_set=data_set, value=zero_one)
    csvMethods.add_column(row_index=5, column_name='$x_2$', data_set=data_set, value=zero_two)
    return


add_delta_col()
data = polynomialMaths.data_dropped_negatives(data_set=data_frame, col_index=3)
calculate_zeros(data_set=data)
csvMethods.save_output(data=data, filename='python_fun.csv', separator=';')
