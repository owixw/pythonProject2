from app.io.input import read_from_file, read_from_file_using_pandas
import pandas as pd
import pytest


def test_format_read_from_file():
    data = read_from_file("tests/data_test/input_test")
    assert isinstance(data, str)


def test_read_from_file():
    actual_data = read_from_file("tests/data_test/input_test")
    expected_data = ("Reading practice to help you understand long, complex texts about a wide variety of topics, "
                     "some of which may be unfamiliar.")
    assert actual_data == expected_data


def test_read_from_file_exception():
    with pytest.raises(FileNotFoundError):
        read_from_file("Some_file")


def test_format_read_from_file_using_pandas():
    data = read_from_file_using_pandas("tests/data_test/username_test.csv")
    assert isinstance(data, pd.DataFrame)


def test_read_from_file_using_pandas():
    actual_data = read_from_file_using_pandas("tests/data_test/username_test.csv")
    expected_data = pd.DataFrame([["booker12", "Rachel", "Booker"], ["grey07", "Laura", "Grey"]],
                                 columns=["Username", "Firstname", "Lastname"])
    pd.testing.assert_frame_equal(actual_data, expected_data)


def test_read_from_file_using_pandas_exception():
    with pytest.raises(FileNotFoundError):
        read_from_file("Some_file")
