import uuid


def generate_uuid():
    return str(uuid.uuid4())

def dao_create_job(job):
    if not job.id:
        job.id = generate_uuid()

    job.save()
