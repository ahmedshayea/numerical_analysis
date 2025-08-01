"""
This module contains a simple implementation of the bisection method for approximating
the solution to a single-variable equation f(x) = 0.

the main function is `solve_with_bisection`, which takes a function 'f', two bounds 'a' and 'b', 
and the number of decimal digits to round the result to. 

you must define the function 'f' as regular python function ( def f(x): ... ).
"""

from typing import Literal
from math import log, cos, sqrt


signType = Literal["negative", "positive"]


def get_sign(f, value) -> signType:
    """
    Well, this is a self descriptive function, it returns the sign of f(value).
    If f(value) is greater than 0, it returns 'positive', otherwise it returns 'negative'.
    """
    return "positive" if f(value) > 0 else "negative"


def validate_ab_value(f, a, b):
    """
    f([a, b]) sign must be of a different type
    """

    # check if a or b is already a solution
    if f(a) == 0:
        raise ValueError("Equation has been solved")

    if f(b) == 0:
        raise ValueError("Equation has been solved")

    # check if f(a) and f(b) have different signs
    return f(a) * f(b) < 0


def num_of_iterations(a: float, b: float, to_decimal_digit: int):
    """
    Determine the number of iterations required to reach certain percision error rate

    Note: I had to use abs ( absolute value) of the below equation because it produces
    negative value, currently I am not sure why , but I will look into it later.

    Note: b - a must be wrapped insdie abs ( absolute value ) to tolerate with cases where b is less than a
    which produce a negative result and negative results doesn't have log!. 
    """
    epsilon = 10 ** (-to_decimal_digit)
    return round((log(abs(b - a)) - log(epsilon)) / log(2))


def solve_with_bisection(
    f, a, b, to_decimal_digit: int = 10,
):
    """
    solve a single-variable equation by using bisection method, approximate the solution 
    up to 'to_decimal_digit'
parameters:
        f: function to solve, must be a single variable Function

        a: left bound of the interval
        b: right bound of the interval

        to_decimal_digit:
        the number of decimal digits to round the result to,
        this function will find the solution to that decimal digit, for example,
        if to_decimal_digit = 10, the function will return a solution that is
        accurate to 10 decimal digits.


    returns:
        c: the solution to the equation f(x) = 0,
        rounded to the specified number of decimal digits.

    Note:
        this function uses recursion to find the solution,
        if you don't know what recursion is, it is simply the function calling itslef
        with different parameters until it reaches a base case,
        when it do reach the base case ( when it finds the solution in this case ),
        it will return that solution and stop calling itself.
    """

    # Find center point c
    c = (a + b) / 2

    print("c = ", c)

    # This is recursion base case ( f(c) == 0 ) 
    if round(f(c), to_decimal_digit) == 0:
        return c

    assert validate_ab_value(f, a, b)
    a_sign = get_sign(f, a)

    if get_sign(f, c) == a_sign:
        a = c
    else:
        b = c

    return solve_with_bisection(
        f, a, b, to_decimal_digit,
    )


def f(x):
    return (x**4) + 4*(x**2) - 10

# Sample functions to test the bisection method
def f1(x):
    return (x**2) + x - 3


def f2(x):
    return x**3 + x - 1


def f3(x):
    return cos(x) - x

def excer(x: float) -> float:
    return sqrt(x) - cos(x)


def main():
    # define bounds for the bisection method
    a = 0
    b = 1

    to_decimal_digit = 2

    c = solve_with_bisection(excer, a, b, to_decimal_digit)
    n = num_of_iterations(a, b, to_decimal_digit)

    print("Solution is: ", c)
    print("Number of iterations: ", n)
    print("Function at c:  ", excer(c))
    print(f"b - a / 2^{n} = ", (b - a) / 2**n)


if __name__ == "__main__":
    main()
