"""
    infa.exceptions
    ~~~~~~~~~~~~~~~

    Infa exceptions.

"""

class InfaError(Exception):
    """Baseclass for all Infa errors."""

    pass

class InfaPmrepError(InfaError):
    """Raised if a pmrep error occurs."""

    pass
