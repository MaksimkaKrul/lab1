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

def interactive_mode():
    while True:
        try:
            a = float(input("a = "))
            if a == 0:
                raise ValueError("a cannot be 0")
            break
        except ValueError as e:
            print(f"Error. Expected a valid real number, got {e}")

    b = float(input("b = "))
    c = float(input("c = "))
    solve_quadratic(a, b, c)

def file_mode(filename: str):
    try:
        with open(filename, 'r') as file:
            data = file.read().strip()
            a, b, c = map(float, data.split())
            solve_quadratic(a, b, c)
    except FileNotFoundError:
        print(f"Error. file {filename} does not exist", file=sys.stdout)
        sys.exit(1)
    except ValueError:
        print("Error. invalid file format", file=sys.stdout)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        interactive_mode()
    elif len(sys.argv) == 2:
        file_mode(sys.argv[1])
    else:
        print("Usage: python quadratic_solver.py [filename]", file=sys.stdout)
        sys.exit(1)