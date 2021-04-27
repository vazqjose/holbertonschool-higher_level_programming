#!/usr/bin/python3
for n in range(0, 99):
    if n < 10:
        print('{:0>2d}, '.format(n), end='')
    else:
        print('{}, '.format(n), end='')
print('99')
