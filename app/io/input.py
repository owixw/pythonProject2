import pandas as pd


def input_from_console():
    """
    Input the user's input from the console.

    Returns:
        str: The user's input from the console.
    """
    text = input("Please enter your text: ")
    return text


def read_from_file(file_path):
    """
    Read text from given file using Python's built-in functions.

    Args:
        file_path (str): The path to the file from which to read the text.

    Returns:
        str: The text read from the file.
    """
    with open(file_path, mode="r") as f:
        text = f.read()
    return text


def read_from_file_using_pandas(file_path):
    """
    Read text from given file using Pandas lib.

    Args:
        file_path (str): The path to the file from which to read the text.

    Returns:
        str: The text read from the file.
    """
    text = pd.read_csv(file_path)
    return text
