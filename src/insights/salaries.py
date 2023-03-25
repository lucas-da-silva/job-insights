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
    try:
        if job["min_salary"] > job["max_salary"]:
            raise ValueError

        return job["min_salary"] <= int(salary) <= job["max_salary"]
    except:
        raise ValueError


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError
