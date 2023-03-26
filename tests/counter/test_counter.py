from unittest.mock import mock_open, patch
from src.pre_built.counter import count_ocurrences

PATH = "data/jobs.csv"
WORDS = ["Javascript", "Python"]
COUNT_WORD = [2, 3]


def test_counter():
    jobs = """Python, 
    Java, 
    JavaScript, 
    HTML, CSS, 
    React, Redux, Python, 
    JavaScript, Python
    """

    with patch("builtins.open", mock_open(read_data=jobs)):
        for index, word in enumerate(WORDS):
            assert count_ocurrences(PATH, word) == COUNT_WORD[index]
