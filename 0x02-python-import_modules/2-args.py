#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    outputs = ["argument", "arguments"]
    argc = len(argv)
    if argc == 2:
        print("{} {}.".format((argc - 1), outputs[0]))
    else:
        print("{} {}:".format((argc - 1), outputs[1]))
        i = 1
        while i < argc:
            print("{}: {}".format(i, argv[i]))
            i += 1
