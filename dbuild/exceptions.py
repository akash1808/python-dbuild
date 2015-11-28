class DbuildException(Exception):
    pass


class DbuildDockerBuildFailedException(DbuildException):
    fmt = '''Docker build failed

Error message: %s

Full build messages

%s'''

    def __init__(self, msg, details):
        self.msg = msg
        self.details = details

    def __str__(self):
        return self.fmt % (self.msg, self.details)


class DbuildBuildFailedException(DbuildException):
    pass


class DbuildSourceBuildFailedException(DbuildException):
    pass


class DbuildBinaryBuildFailedException(DbuildException):
    pass
