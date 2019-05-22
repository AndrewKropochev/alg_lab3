#!/usr/bin/env python
# -*- coding: utf-8 -*-


def linear_search(data, value):
    for i, v in enumerate(data):
        if v > value:
            return None
        if v == value:
            return i
    return None


def binary_search(data, value):
    mid = len(data) // 2
    low = 0
    high = len(data) - 1
     
    while data[mid] != value and low <= high:
        if value > data[mid]:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2
     
    if low > high:
        return None
    else:
        return mid


    """
    тест
    """
gag = [1,5,34,45,55,56,67,79,88,887,895,910,1000]
print(binary_search(gag,34))

