#!/usr/bin/python3

if __name__ == "__main__":

    import hidden_4
    myArr = dir(hidden_4)
    length = len(myArr)

    for n in myArr:
        if n[0] != '_' and n[1] != '_':
            print('{}'.format(n))
