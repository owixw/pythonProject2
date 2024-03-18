import pandas as pd


def output_to_console(text):
    """
    Output the user's input to the console.

    Args:
        text (Any): The user's input.
    """
    print(text)


def write_to_file(text, file_path):
    """
    Write given text to the file using Python's built-in functions.

    Args:
        text (str): The text to be written to the file.
        file_path (str): The path to the file to which to write the text.
    """
    with open(file_path, "a") as f:
        f.write(text)


def write_to_file_using_pandas(data_frame, file_path):
    """
    Write given text to the file using Pandas lib.

    Args:
        data_frame (df): The data frame to be written to the file.
        file_path (str): The path to the file to which to write the text.
    """
    data_frame.to_csv(file_path, mode="a")
