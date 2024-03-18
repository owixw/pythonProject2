
from app.io.input import input_from_console, read_from_file, read_from_file_using_pandas
from app.io.output import output_to_console, write_to_file, write_to_file_using_pandas


def main():
    result_from_input = input_from_console()
    output_to_console(result_from_input)
    write_to_file(result_from_input, "./data/output")

    result_from_file = read_from_file("./data/input")
    output_to_console(result_from_file)
    write_to_file(result_from_file, "./data/output")

    result_from_file_using_pandas = read_from_file_using_pandas("./data/username.csv")
    output_to_console(result_from_file_using_pandas)
    write_to_file_using_pandas(result_from_file_using_pandas, "./data/output")


if __name__ == '__main__':
    main()
