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

DOMAIN_TABLES = {
    "DEPARTMENTS": department_table,
    "HIRED_EMPLOYEES": hired_employee_table,
    "JOBS": job_table,
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