import sys, math

def solve_quadratic(a: float, b: float, c: float):
    if a == 0:
        print("Error. a cannot be 0", file=sys.stdout)
        sys.exit(1)
    
    discriminant = (b ** 2) - (4 * a * c)
    squared_d = math.sqrt(discriminant)
    
    print(f"Solving equation: {a}x^2 + {b}x + {c} = 0")
    
    if squared_d > 0:
        x1 = (-b + (math.sqrt(squared_d))) / (2 * a)
        x2 = (-b - (math.sqrt(squared_d))) / (2 * a)
        print("There are 2 real roots.")
        print(f"x1 = {x1}, x2 = {x2}")

    elif squared_d == 0:
        x = (-b) / (2 * a)
        print("There is exactly 1 real root.")
        print(f"x = {x}")

    else:
        print("No real roots exist for this equation.")

