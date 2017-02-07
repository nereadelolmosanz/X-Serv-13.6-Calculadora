#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
 Nerea Del Olmo Sanz - GITT
 Ejercicio 13.6
 Calculadora - Corregido
"""


import sys


def add(op1, op2):
    return op1 + op2


def substract(op1, op2):
    return op1 - op2


def multiply(op1, op2):
    return op1 * op2


def divide(op1, op2):
    try:
        return float(op1) / op2
    except ZeroDivisionError:
        print("Cannot divide by zero")


if __name__ == "__main__":

    if len(sys.argv) != 4:
        sys.exit("Usage: $ python calculadora.py function op1 op2")

    function = sys.argv[1]
    functions = ["add", "substract", "multiply", "divide"]

    if function not in functions:
        sys.exit("add - substract - multiply - divide")

    try:
        operand1 = int(sys.argv[2])
        operand2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Only integer numbers")

    if function == "add":
        print add(operand1, operand2)

    if function == "substract":
        print substract(operand1, operand2)

    if function == "multiply":
        print multiply(operand1, operand2)

    if function == "divide":
        print divide(operand1, operand2)
