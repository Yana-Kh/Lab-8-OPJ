#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # Ввести кортеж одной строкой.
    A = tuple(map(int, input().split()))

    # Найти искомую сумму.
    ind = 0
    for i, value in enumerate(A):
        if value % 2 == 0:
            ind = i
            if A[i+1] % 2 == 0:
                print(f"Найдена пара, начиная с индекса: {ind}")
                exit(0)
