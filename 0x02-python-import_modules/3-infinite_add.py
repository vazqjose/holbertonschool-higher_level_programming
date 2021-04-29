#!/usr/bin/python
if __name__ == "__main__":

    import sys
    argv = sys.argv
    arglen = len(argv)
    suma = 0

    for n in range(1, arglen):
        suma += int(argv[n])

    print(suma)
