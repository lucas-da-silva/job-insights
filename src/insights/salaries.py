from typing import Union, List, Dict

from src.insights.jobs import read
from src.validations.salaries import (
    validation_matches_salary,
    validation_filter_by_salary,
)


def get_max_salary(path: str) -> int:
    jobs = read(path)
    all_salary = [
        int(job["max_salary"]) for job in jobs if job["max_salary"].isdigit()
    ]
    return max(all_salary)


def get_min_salary(path: str) -> int:
    jobs = read(path)
    all_salary = [
        int(job["min_salary"]) for job in jobs if job["min_salary"].isdigit()
    ]
    return min(all_salary)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    if validation_matches_salary(job):
        return job["min_salary"] <= int(salary) <= job["max_salary"]

    raise ValueError


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    jobs_filtered = [
        job
        for job in jobs
        if validation_filter_by_salary(job, salary)
        and matches_salary_range(
            {
                "max_salary": int(job["max_salary"]),
                "min_salary": int(job["min_salary"]),
            },
            salary,
        )
    ]

    return jobs_filtered
