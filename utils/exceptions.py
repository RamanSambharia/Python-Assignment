class FileLoadingError(Exception):
    """Raised when CSV files fail to load properly."""
    pass


class MatchingError(Exception):
    """Raised when function matching fails."""
    pass


class DeviationCheckError(Exception):
    """Raised when deviation checking fails."""
    pass


class DatabaseError(Exception):
    """Raised for database-related issues."""
    pass
