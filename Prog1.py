#!/usr/bin/python3
def factorial(n):
    fact = 1
    for i in range(n+1):
        fact*=i
    return fact