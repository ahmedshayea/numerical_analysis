from typing import Literal
from math import log, cos


def f(x):
    return (x**3) + 4*(x**2) - 10

signType = Literal['negative', 'positive']

def get_sign(f, value) -> signType:
    return 'positive' if f(value) > 0 else 'negative'

def validate_ab_value(f, a, b):
    """
    f([a, b]) sign must be of a different type
    """

    if f(a) == 0:
        raise ValueError("Equation has been solved")

    if f(b) == 0:
        raise ValueError("Equation has been solved")

    
    a_sign = get_sign(f, a)
    b_sign = get_sign(f, b)

    if a_sign == b_sign:
        return False

    return True

def num_of_iterations(a:int, b: int, error_rate: int):
    """
    Determine the number of iterations required to reach certain percision error rate
    """
    return round(abs((log(abs(b - a)) - log(10**error_rate))) / log(2))


def solve_with_bisection(f, a, b, error_rate: int):
    """
    solve given on variable equation by using bisection numerical method.
    """

    # calculate c value
    c = (a + b) / 2



    # check if c satisfy the condition f(c) = 0
    if round(f(c), error_rate) == 0:
        return c

    assert validate_ab_value(f, a, b)

    a_sign = get_sign(f, a)

    if get_sign(f, c) == a_sign:
        a = c
    else: # f(a) sign doesn't equal a_sign, it must equal b_sign
        b = c

    return solve_with_bisection(f, a, b, error_rate)

def o(x):
    return (x**2) + x - 3

def t(x):
    return x**3 + x - 1

def solo(x):
    return cos(x) - x

def main(): 
    a = 0
    b = 1

    error_rate = 10

    c = solve_with_bisection(t, a, b, error_rate)

    print("Solution is: ", c)
    print("Number of iterations: ", num_of_iterations(a, b, error_rate))
    print("Function at c:  ", t(c))

if __name__ == "__main__":
    main()
