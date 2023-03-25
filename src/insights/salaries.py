from typing import Union, List, Dict

from src.insights.jobs import read

# from jobs import read


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
    if (
        "max_salary" in job
        and "min_salary" in job
        and type(job["max_salary"]) == int
        and type(job["min_salary"]) == int
        and job["max_salary"] > job["min_salary"]
    ):
        return job["min_salary"] <= int(salary) <= job["max_salary"]

    raise ValueError


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    jobs_filtered = []

    for job in jobs:
        if job["max_salary"] > job["min_salary"] and salary.isnumeric():
            if matches_salary_range(job, salary):
                jobs_filtered.append(job)

    return jobs_filtered
