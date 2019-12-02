from flask import request
from werkzeug.exceptions import BadRequest


def validate(self, req=None, strict=False):
    if req is None:
        req = request

    result = self.result_class()

    # A record of arguments not yet parsed; as each is found among self.args, it will be popped out
    req.unparsed_arguments = dict(self.argument_class('').source(req)) if strict else {}
    errors = {}
    for arg in self.args:
        value, found = arg.parse(req, self.bundle_errors)
        if isinstance(value, ValueError):
            errors.update(found)
            found = None
        if found or arg.store_missing:
            result[arg.dest or arg.name] = value
    if errors:
        data = {
            "errors": errors,
            "message": "Invalid data",
        }
        bad_request = BadRequest()
        bad_request.data = data

        raise bad_request

    if strict and req.unparsed_arguments:
        arguments = ', '.join(req.unparsed_arguments.keys())
        msg = 'Unknown arguments: {0}'.format(arguments)
        raise BadRequest(msg)

    return result

