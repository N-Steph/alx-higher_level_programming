#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    outputs = ["argument", "arguments"]
    argc = len(argv)
    if argc == 1:
        print("{} {}.".format(argc, outputs[0]))
    else:
        print("{} {}:".format(argc, outputs[1]))
        i = 0
        for argument in argv:
            print("{}: {}".format(++i, argument))
