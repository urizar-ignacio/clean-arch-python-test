import pytest 
from src.usecase.load_data import load_data_to_domain

class MockDataBaseRepo:
    def save(*args, **kwargs):
        return "OK"

    def get_all(*args, **kwargs):
        return []

def generate_sample_jobs_list():
    sample_list = [
        ["A", "Job 1"],
        ["2", "Job 2"],
        ["3", "Job 3"],
    ]
    return sample_list

def test_load_data_unsupported_domain():
    domain = "UNSUPPORTED_DOMAIN"
    with pytest.raises(ValueError, match="Unsupported domain"):
        load_data_to_domain(domain, [], MockDataBaseRepo())

def test_load_data_jobs():
    domain = "JOBS"
    status = load_data_to_domain(domain, generate_sample_jobs_list(), MockDataBaseRepo())
    assert status == "OK"