#!/usr/bin/python3
def safe_print_division(a, b):
    """
    Divides 2 integers and prints the result
    Returns value of the division
    """
    try:
        result = a / b
    except Exception:
        result = None
        pass
    finally:
        print("Inside result: {}".format(result))
    return (result)
