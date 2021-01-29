#!/usr/bin/python3
def commonChars(A):
    set_letters = set(''.join(A))
    all_letters = list(''.join(A))
    list_A = sorted(list(A[1]))
    set_A = sorted(list(set(A[1])))

    for counter, value in enumerate(list(''.join(A)), 1):
        print(counter)
        print(value)

