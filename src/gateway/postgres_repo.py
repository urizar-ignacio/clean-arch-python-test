from sqlalchemy import (column, table, create_engine, insert, select)

# TABLES
department_table = table("department",
                         column("id"),
                         column("department"))
hired_employee_table = table("hired_employee",
                             column("id"),
                             column("name"),
                             column("datetime"),
                             column("department_id"),
                             column("job_id"))
job_table = table("job",
                  column("id"),
                  column("job"))

# VIEWS
employees_by_quarter_view = table("employees_by_quarter",
                             column("department"),
                             column("job"),
                             column("q1"),
                             column("q2"),
                             column("q3"),
                             column("q4"))
employees_over_mean_view = table("employees_over_mean",
                            column("id"),
                            column("department"),
                            column("hired"))

DOMAIN_TABLES = {
    "DEPARTMENTS": department_table,
    "HIRED_EMPLOYEES": hired_employee_table,
    "JOBS": job_table,
}

REPORT_VIEWS = {
    "employees_by_quarter": employees_by_quarter_view,
    "employees_over_mean": employees_over_mean_view
}
REPORT_HEADERS = {
    "employees_by_quarter": [
        "department",
        "job",
        "q1",
        "q2",
        "q3",
        "q4"
    ],
    "employees_over_mean": [
        "id",
        "department",
        "hired"
    ]
}

class PostgresRepo:
    CONN_STRING = "postgresql+psycopg2://postgres:postgres@db:5432/postgres"

    def start_engine(self):
        engine = create_engine(self.CONN_STRING)
        return engine

    def save(self, objects_to_load, domain):
        records = [obj.dict() for obj in objects_to_load]
        query = insert(DOMAIN_TABLES[domain])
        engine = self.start_engine()
        with engine.connect() as conn:
            result = conn.execute(query, records)
            conn.commit()
        return "OK"
    
    def get_all(self, domain):
        query = select(DOMAIN_TABLES[domain])
        engine = self.start_engine()
        with engine.connect() as conn:
            results = conn.execute(query)
        return results
    
    def get_report(self, view):
        header = REPORT_HEADERS[view]
        query = select(REPORT_VIEWS[view])
        engine = self.start_engine()
        with engine.connect() as conn:
            results = conn.execute(query)
        results_list = [list(row) for row in results.all()]
        return (header, results_list)