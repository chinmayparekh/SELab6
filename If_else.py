#!/usr/bin/python3
def factorial(x):
    fact = 1
    for i in range(1,x+1):
        fact *= i
    return fact
