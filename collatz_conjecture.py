#!/usr/bin/env python
def collatz(n):
    c = 0
    while True:
        c = c +1
        # print n
        if n == 1:
            break
        if n % 2 ==0:
            n = n / 2
        else:
            n = 3 * n + 1
    return c

def find_longest_sequence(max):
    record_n = 1
    record_sequence = 0
    c = 1
    while c < max:
        if c % 10000 == 0:
            print c
        if collatz(c) > record_sequence:
            record_n = c
            record_sequence = collatz(c)
        c = c + 1
    print "the record number is: "
    print record_n
    print "the record sequence is of length: "
    print record_sequence


if __name__ == '__main__':
    # print collatz(13)
    find_longest_sequence(1000000)
