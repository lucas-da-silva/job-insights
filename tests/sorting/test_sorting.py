from src.pre_built.sorting import sort_by


jobs = [
    {
        "min_salary": 4000,
        "max_salary": 8000,
        "date_posted": "2020-04-25",
    },
    {
        "min_salary": 1000,
        "max_salary": 3000,
        "date_posted": "2019-03-10",
    },
]

jobs_sorted_min_salary = [
    {
        "min_salary": 1000,
        "max_salary": 3000,
        "date_posted": "2019-03-10",
    },
    {
        "min_salary": 4000,
        "max_salary": 8000,
        "date_posted": "2020-04-25",
    },
]

jobs_sorted_max_salary = [
    {
        "min_salary": 4000,
        "max_salary": 8000,
        "date_posted": "2020-04-25",
    },
    {
        "min_salary": 1000,
        "max_salary": 3000,
        "date_posted": "2019-03-10",
    },
]

jobs_sorted_date_posted = [
    {
        "min_salary": 4000,
        "max_salary": 8000,
        "date_posted": "2020-04-25",
    },
    {
        "min_salary": 1000,
        "max_salary": 3000,
        "date_posted": "2019-03-10",
    },
]


def test_sort_by_criteria():
    sort_by(jobs, "min_salary")
    assert jobs == jobs_sorted_min_salary

    sort_by(jobs, "max_salary")
    assert jobs == jobs_sorted_max_salary

    sort_by(jobs, "date_posted")
    assert jobs == jobs_sorted_date_posted
