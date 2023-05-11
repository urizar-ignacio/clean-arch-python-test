from flask import request
from flask_restful import Resource
from src.gateway.postgres_repo import PostgresRepo
from src.usecase.load_data import load_data_to_domain

from csv import reader
from io import StringIO


def file_object_to_list(file):
    file_object = StringIO(file.read().decode())
    rows = []
    csv_reader = reader(file_object)
    for row in csv_reader:
        print(row, flush=True)
        rows.append(row)
    return rows

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
        if "file" not in request.files:
            return {"BAD_REQUEST": "No file attached to POST request"}, 400
        
        file = request.files["file"]
        if not file.filename.endswith(".csv"):
            return {"BAD_REQUEST": "File extension not supported. Must be .csv"}, 400
        
        print(type(file), flush=True)
        rows = file_object_to_list(file)

        if len(rows) > 0:
            postgres_repo = PostgresRepo()
            result = load_data_to_domain(self.DOMAIN, rows, postgres_repo)
            return result, 200
        else:
            return {"BAD_REQUEST": "Empty file"}, 400
