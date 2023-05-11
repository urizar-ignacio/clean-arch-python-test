from datetime import datetime
from pydantic import BaseModel

class HiredEmployee(BaseModel):
    id: int
    name: str
    datetime: datetime
    department_id: int
    job_id: int
