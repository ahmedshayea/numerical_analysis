from sympy import symbols, diff, lambdify

def symbolic_derivative(f_expr):
    """
    Return a function that computes the symbolic derivative.
    """
    x = symbols('x')
    f_prime_expr = diff(f_expr, x)
    return lambdify(x, f_prime_expr)
