"""
This module provides a decorator that adds exception handling to functions.
"""
import logging

def logged(exception, mode):
    """
    Parameterized decorator that adds exception handling to functions
    and logs them based on the specified mode.
    Parameters:
    exception (Exception): Class or tuple of classes of exceptions to be caught.
    mode (str): Logging mode: "console" or "file".
    Returns:
    wrapper (function): Wraps the input function and adds exception handling.
    """
    def decorator(func):
        """
        Inner decorator that wraps the input function.
        Parameters:
        func (function): The input function to be wrapped.
        Returns:
        wrapper (function): Wraps the input function and adds exception handling.
        """
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception as exception_instance:
                logging.basicConfig(filename='exception.txt',
                                    level=logging.ERROR, format='%(levelname)s:%(message)s')
                if mode == "console":
                    logging.exception("Caught exception: %s", exception_instance)
                elif mode == "file":
                    logging.exception("Caught exception: %s", exception_instance)
                return None
        return wrapper
    return decorator
