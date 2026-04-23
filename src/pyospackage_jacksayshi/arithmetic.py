"""
A module that adds numbers together.

You may want to delete this module or modify it for your package.
It's generally good practice to have a docstring
that explains the purpose of the module, at the top.
"""

def add_numbers(a, b):
    """
    Add two numbers together and return the result.

    This is an example function with a numpy style docstring.
    We recommend using this style for consistency and readability.

    Parameters
    ----------
    a : float
        The first number to add.
    b : float
        The second number to add.

    Returns
    -------
    float
        The sum of the two numbers.

    Examples
    --------
    >>> add_numbers(3, 5)
    8
    >>> add_numbers(-2, 7)
    5

    """
    return a + b


def sub_numbers(a, b):
    """
    Subtract second number from first 
    and return the result
    
    """
    # 1. Check that arguments were actually provided (not None)
    if a is None or b is None:
        raise ValueError("Both arguments must be provided, got None")

    # 2. Check that both inputs are numbers
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError(f"Expected numbers, got {type(a).__name__} and {type(b).__name__}")

    return a-b 