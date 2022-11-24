#!/usr/bin/python3
def factorial(x):
    fact = 1
    for i in range(x+1):
        fact *= i
    return fact
