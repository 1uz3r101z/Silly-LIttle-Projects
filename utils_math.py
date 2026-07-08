#utils_math.py
def add(a, b):
    """Return the sum of two numbers."""
    return a + b
def multiply(a,  b):
    """Return the product of two numbers."""
    return a * b
def avergare(numbers):
    """Return the average of a list of numbers."""
    if not numbers:
        return None
    return sum(numbers)/len(numbers)