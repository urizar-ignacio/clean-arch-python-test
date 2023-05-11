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
