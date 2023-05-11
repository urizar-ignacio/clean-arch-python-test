from src.entity.job import Job
from pydantic.error_wrappers import ValidationError

ALLOWED_DOMAINS = [
    "JOBS",
]

ENTITIES_DATA_TYPES = {
    "JOBS": Job
}

ENTITIES_HEADERS = {
    "JOBS": [
        "id",
        "job"
    ]
}

def load_data_to_domain(domain, records, repo):
    if domain not in ALLOWED_DOMAINS:
        raise ValueError("Unsupported domain")
    entity = ENTITIES_DATA_TYPES[domain]
    objects_to_load = []
    failed_records = []
    for record in records:
        record_dict = dict(zip(ENTITIES_HEADERS[domain], record))
        try:
            objects_to_load.append(entity(**record_dict))
        except ValidationError as e:
            failed_records.append(record)

    #TODO: Implement Logger
    if len(failed_records) > 0:
        print(f"This records does not meet Data Rules: {failed_records}", flush=True)
    result = repo.save(objects_to_load, domain)
    print(objects_to_load, flush=True)
    return result