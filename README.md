# Data Engineer Test
### Ignacio Urízar
### May, 2023

## Objective
POC project build on Python/Flask. This app load CSV files into a PostgreSQL Data Base.

## Features:
### Load data endpoints:
For each domain [Jobs, Departments, Hired Employees] this services exposes an endpoint:

- `POST: 0.0.0.0/api/jobs`
- `POST: 0.0.0.0/api/departments`
- `POST: 0.0.0.0/api/hired_employees`

The body of the request must containd a CSV file attached with less than 1000 rows.

### Get reports
There are two report build up in this services. These reports, are based on Views on PostgreSQL and can be obtained with the following endpoints:
- `GET: 0.0.0.0/api/employees_by_quarter`
- `GET: 0.0.0.0/api/employees_over_mean`
