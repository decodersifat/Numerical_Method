import math as mt

def f(x):
    return 3 * x - mt.cos(x) - 1


def bisection_method(a, b, tolerance):
    while (b - a) / 2 > tolerance:
        c = (a + b) / 2
        if f(c) * f(a) > 0:
            a = c
        else:
            b = c
    return c


def regula_falsi(a, b, tolerance):
    while (b - a) / 2 > tolerance:
        c = ((a * f(b)) - (b * f(a))) / (f(b) - f(a))
        if f(a) * f(c) > 0:
            a = c
        else:
            b = c
    return c


def secant_method(x0, x1, tol, max_iter=100):
    while max_iter:
        Xnext = x1 - ((x1 - x0) / (f(x1) - f(x0))) * f(x1)

        if abs(Xnext - x1) < tol:
            return x1
        else:
            x0 = x1
            x1 = Xnext
        max_iter = max_iter - 1

    return Xnext


if __name__ == "__main__":
    a = 0
    b = 1
    tolerance = 1e-6

    #    root = bisection_method(a, b, tolerance)
    #    root = regula_falsi(a, b, tolerance)
    root = secant_method(1, 0, tolerance)
    print("The root of the function is approximately:", root)
