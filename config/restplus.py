import os


class Restplus:
    BUNDLE_ERRORS = os.getenv('BUNDLE_ERRORS', True)

    RESTPLUS_VALIDATE = os.getenv('RESTPLUS_VALIDATE', True)
