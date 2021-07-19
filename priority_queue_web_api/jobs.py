from typing import Dict
from flask import Blueprint, request, jsonify

from . import db
from .queue import queue
from .schemas import job_schema
from .dao.jobs_dao import dao_create_job
from .models import Job
from .exceptions import ApiValidationException, ApiUnprocessableException


bp = Blueprint('jobs', __name__)

@bp.route('/jobs/next', methods=['GET'])
def get_next():
    if queue.head:
        next = queue.head.data
        return jsonify(next.serialize_get()), 200
    else:
        return jsonify({"jobId": None, "message": "There are currently no jobs enqueue"}), 200

@bp.route('/jobs', methods=['POST'])
def create():
    try:
        req = request.get_json()
        validate_request(req)
        job = Job(name=req['name'],
                        priority=req['priority'],
                        submitterId=req['submitterId'])
        dao_create_job(job)

        if job is None:
            raise ApiUnprocessableException(message=f"Could not create job for submitted data {req}")
        
        queue.enqueue(job)

    except ApiValidationException as err:
        return jsonify(err.serialize()), err.status_code
    except ApiUnprocessableException as err:
        return jsonify(err.serialize()), err.status_code
    else:
        return jsonify(job.serialize_post()), 201


def validate_request(request: Dict) -> Exception:
    is_not_valid = job_schema.validate(request, session=db.session)
    
    if bool(is_not_valid):
        raise ApiValidationException(message=f"{is_not_valid}")
