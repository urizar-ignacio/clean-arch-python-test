from flask import Flask
from flask_restful import Api

from src.gateway.endpoint import Department, HiredEmployee, Jobs, EmployeesByQuarter, EmployeesOverMean

app = Flask(__name__)
api = Api(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!!!</p>"

# DOMAINS
api.add_resource(Department, '/api/departments/')
api.add_resource(HiredEmployee, '/api/hired_employees/')
api.add_resource(Jobs, '/api/jobs/')

# REPORTS
api.add_resource(EmployeesByQuarter, '/api/employees_by_quarter/')
api.add_resource(EmployeesOverMean, '/api/employees_over_mean/')

if __name__ == "__main__":
    app.run(debug=True)
