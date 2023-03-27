from src.pre_built.brazilian_jobs import read_brazilian_file
from tests.mocks.brazilians_jobs_english import jobs

PATH = "tests/mocks/brazilians_jobs.csv"


def test_brazilian_jobs():
    assert read_brazilian_file(PATH) == jobs
