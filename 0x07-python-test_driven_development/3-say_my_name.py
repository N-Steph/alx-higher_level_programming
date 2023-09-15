#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    data = {"first_name": first_name, "last_name": last_name}
    for key, value in data.items():
        if type(value) is not str:
            raise TypeError("{} must be a string".format(key))
    print("My name is {} {}".format(first_name, last_name))
