from src.pre_built.sorting import sort_by
from tests.mocks.sorting import (
    jobs,
    jobs_sorted_by_max_salary,
    jobs_sorted_by_min_salary,
    jobs_sorted_by_date_posted,
)


def test_sort_by_criteria():
    sort_by(jobs, "min_salary")
    assert jobs == jobs_sorted_by_min_salary

    sort_by(jobs, "max_salary")
    assert jobs == jobs_sorted_by_max_salary

    sort_by(jobs, "date_posted")
    assert jobs == jobs_sorted_by_date_posted
