import math

class QuadraticEquationSolver:
    def findRoots(self, a, b, c):
        if a == 0:
            return "Not a quadratic equation (a cannot be 0)."
        
        discriminant = b**2 - 4*a*c

        if discriminant > 0:
            root1 = (-b + math.sqrt(discriminant)) / (2 * a)
            root2 = (-b - math.sqrt(discriminant)) / (2 * a)
            return f"Two real and distinct roots: {root1}, {root2}"
        elif discriminant == 0:
            root = -b / (2 * a)
            return f"One real and equal root: {root}"
        else:
            real = -b / (2 * a)
            imag = math.sqrt(-discriminant) / (2 * a)
            return f"Complex roots: {real} + {imag}i and {real} - {imag}i"

# Example usage
solver = QuadraticEquationSolver()
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

result = solver.findRoots(a, b, c)
print(result)
