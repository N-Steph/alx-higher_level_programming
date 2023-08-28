#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """
    Divides element by element my_list_1 and my_list_2
    Returns a new list with all divisions
    """
    new_list = []
    i = 0
    while (i < list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            result = 0
            print("division by 0")
        except (ValueError, TypeError):
            result = 0
            print("wrong type")
        except IndexError:
            result = 0
            print("out of range")
        finally:
            new_list.append(result)
        i += 1
    return (new_list)
