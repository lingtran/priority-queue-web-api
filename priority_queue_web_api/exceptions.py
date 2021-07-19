class ApiBaseException(Exception):
    status_code = 422

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def serialize(self):
        response = dict(self.payload or ())
        response['message'] = self.message
        response['status_code'] = self.status_code
        return response


class ApiValidationException(ApiBaseException):
    pass


class ApiUnprocessableException(ApiBaseException):
    pass
