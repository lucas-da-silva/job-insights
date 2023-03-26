from typing import Dict, Union


def validation_filter_by_salary(job: Dict, salary: Union[str, int]) -> bool:
    if (
        str(salary).isnumeric()
        and str(job["max_salary"]).isnumeric()
        and str(job["min_salary"]).isnumeric()
        and int(job["max_salary"]) > int(job["min_salary"])
    ):
        return True

    return False


def validation_matches_salary(job: Dict) -> bool:
    if (
        "max_salary" in job
        and "min_salary" in job
        and type(job["max_salary"]) == int
        and type(job["min_salary"]) == int
        and job["max_salary"] > job["min_salary"]
    ):
        return True

    return False
