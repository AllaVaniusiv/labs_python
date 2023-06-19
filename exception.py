"""
This module defines custom exception classes 
"""
class OutOfPaperException(Exception):
    """
    Custom exception raised when trying to print with no paper.
    This exception is raised when attempting to print a document,
    but the printer has run out of paper.
    Attributes:
    None
    Methods:
    None
    """
