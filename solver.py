import sys, math, cmath

def solve_quadratic(a: float, b: float, c: float):
    if a == 0:
        print("Error. a cannot be 0", file=sys.stdout)
        sys.exit(1)

    discriminant = (b ** 2) - (4 * a * c)

    print(f"Solving equation: {a}x^2 + {b}x + {c} = 0")

    if discriminant > 0:
        squared_d = math.sqrt(discriminant)
        x1 = (-b + squared_d) / (2 * a)
        x2 = (-b - squared_d) / (2 * a)
        print("There are 2 real roots.")
        print(f"x1 = {x1}, x2 = {x2}")

    elif discriminant == 0:
        x = (-b) / (2 * a)
        print("There is exactly 1 real root.")
        print(f"x = {x}")

    else:
        squared_d = cmath.sqrt(discriminant)
        x1 = (-b + squared_d) / (2 * a)
        x2 = (-b - squared_d) / (2 * a)
        print("There are 2 complex roots:")
        print(f"x1 = {x1}, x2 = {x2}")