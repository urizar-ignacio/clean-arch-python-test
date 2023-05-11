from flask import request
from flask_restful import Resource
from src.gateway.postgres_repo import PostgresRepo
from src.usecase.get_report import get_report
from src.usecase.load_data import load_data_to_domain

from csv import reader
from io import StringIO


def file_object_to_list(file):
    file_object = StringIO(file.read().decode())
    rows = []
    csv_reader = reader(file_object)
    for row in csv_reader:
        rows.append(row)
    return rows

def generic_post_method(domain, request):
    if "file" not in request.files:
            return {"BAD_REQUEST": "No file attached to POST request"}, 400
        
    file = request.files["file"]
    if not file.filename.endswith(".csv"):
        return {"BAD_REQUEST": "File extension not supported. Must be .csv"}, 400
    
    rows = file_object_to_list(file)

    if len(rows) <= 0:
        return {"BAD_REQUEST": "Empty file"}, 400
    elif len(rows) > 1000:
        return {"BAD_REQUEST": "Max number of records (1000) excedeed"}, 400
    else:
        postgres_repo = PostgresRepo()
        try:
            result = load_data_to_domain(domain, rows, postgres_repo)
        except ValueError as e:
            return {"ERROR": str(e)}, 500
        return result, 200
    
def generic_get_report(report_name):
    postgres_repo = PostgresRepo()
    results = get_report(postgres_repo, report_name)
    return {"headers": results[0], "data": results[1]}

class Jobs(Resource):
    DOMAIN = "JOBS"

    def get(self):
        return {
            "RESOURCE": "jobs",
            "ALLOWED_METHODS": [
                "GET",
                "POST"
            ]
        }
    
    def post(self):
        return generic_post_method(self.DOMAIN, request)

class Department(Resource):
    DOMAIN = "DEPARTMENTS"

    def get(self):
        return {
            "RESOURCE": "departments",
            "ALLOWED_METHODS": [
                "GET",
                "POST"
            ]
        }

    def post(self):
        return generic_post_method(self.DOMAIN, request)

class HiredEmployee(Resource):
    DOMAIN = "HIRED_EMPLOYEES"

    def get(self):
        return {
            "RESOURCE": "hired_employees",
            "ALLOWED_METHODS": [
                "GET",
                "POST"
            ]
        }

    def post(self):
        return generic_post_method(self.DOMAIN, request)
    
class EmployeesByQuarter(Resource):
    REPORT_NAME = "employees_by_quarter"

    def get(self):
        return generic_get_report(self.REPORT_NAME)

class EmployeesOverMean(Resource):
    REPORT_NAME = "employees_over_mean"

    def get(self):
        return generic_get_report(self.REPORT_NAME)