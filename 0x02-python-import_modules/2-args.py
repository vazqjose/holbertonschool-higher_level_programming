#!/usr/bin/python3
if __name__ == "__main__":

    import sys
    argv = sys.argv
    argLen = len(argv)
    string = "argument"

    if argLen == 1:
        string = string + "s."
    elif argLen == 2:
        string = string + ":"
    elif argLen > 2:
        string = string + "s:"

    print("{} {}".format(argLen - 1, string))

    for n in range(1, argLen):
        print("{}: {}".format(n, argv[n]))
