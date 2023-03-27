from src.pre_built.sorting import sort_by
from tests.mocks.jobs_sorting import (
    jobs,
    jobs_sorted_date_posted,
    jobs_sorted_max_salary,
    jobs_sorted_min_salary,
)


def test_sort_by_criteria():
    sort_by(jobs, "min_salary")
    assert jobs == jobs_sorted_min_salary

    sort_by(jobs, "max_salary")
    assert jobs == jobs_sorted_max_salary

    sort_by(jobs, "date_posted")
    assert jobs == jobs_sorted_date_posted
