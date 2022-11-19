#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # Ввести кортеж одной строкой.
    A = tuple(map(int, input().split()))

    # Найти искомые числа
    f = 0
    for i, value in enumerate(A):
        if value % 2 == 1 and A[i+1] % 2 == 1:
            print(f"Найдена пара, начиная с индекса: {i}")
            f += 1
            break
    if f == 0:
        print("Пары не найдены(")
