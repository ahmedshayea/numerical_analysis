from sympy import symbols, diff, lambdify

def symbolic_derivative(f_expr):
    """
    Return derivative function and the function itself as python functions.
    """
    x = symbols('x')
    f_prime_expr = diff(f_expr, x)
    return lambdify(x, f_prime_expr), lambdify(x, f_expr)


def functionify(f_x):
    x = symbols('x')
    return lambdify(x, f_x)



def solve_with_newton_raphson(func, initial_guess, tolerance=1e-7):
    """
    Solve a root-finding problem using the Newton-Raphson method for single variable equations.
    """

    x_previes = initial_guess
    derivative, function = symbolic_derivative(func)
    x_n = x_previes - (function(x_previes) / derivative(x_previes))

    num_of_iterations = 0

    print(abs(x_n - x_previes) < tolerance)

    while (abs(x_n - x_previes) > tolerance):
        x_previes = x_n
        x_n = x_previes - (function(x_previes) / derivative(x_previes))
        num_of_iterations += 1
        print("loop")

    # return answer value.
    return x_n


def main(): 
    f = "x**2"
    f_x = functionify(f)
    x = solve_with_newton_raphson(f, initial_guess=3)

    print(f"Solution to {f} is :", x)
    round_to = 7
    print(f"Value of '{f}' at {x} rounded to {round_to} digits: {round(f_x(x), round_to)}")

if __name__ == "__main__":
    main()
