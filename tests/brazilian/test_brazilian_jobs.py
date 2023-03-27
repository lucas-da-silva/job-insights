from src.pre_built.brazilian_jobs import read_brazilian_file
from unittest.mock import mock_open, patch
from tests.mocks.brazilians_jobs import brazilians_jobs, english_jobs


def test_brazilian_jobs():
    mocked_jobs = mock_open(read_data="\n".join(brazilians_jobs))

    with patch("builtins.open", mocked_jobs):
        assert read_brazilian_file("PATH") == english_jobs
