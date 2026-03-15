class QuadraticEquation:
    def __init__(self, a=0.0, b=0.0, c=0.0):
        if isinstance(a, QuadraticEquation):
            self.a = a.a
            self.b = a.b
            self.c = a.c
        else:
            self.a = float(a)
            self.b = float(b)
            self.c = float(c)

    def solve(self):
        if self.a == 0.0:
            if self.b == 0.0:
                if self.c == 0.0:
                    return 'inf'
                else:
                    return ()
            x = -self.c/self.b
            return (x,)
        discr = self.b**2 - 4*self.a*self.c
        if discr > 0:
            x1 = (-self.b + discr**0.5) / (2*self.a)
            x2 = (-self.b - discr**0.5) / (2*self.a)
            return (x1, x2)

        if discr == 0:
            x = -self.b/(2*self.a)
            return(x,)
        else:
            return()

    def show(self):
        eq_str = f"{self.a}x^2 + {self.b}x + {self.c}=0"
        eq_str = eq_str.replace("+ -", "-")
        print(eq_str)

def process_equations(filename):
    equations = []
    try:
        with open (filename,"r") as file:
            for line in file:
                parts = line.split()
                if len(parts) == 3:
                    eq = QuadraticEquation(
                        float(parts[0]),
                        float(parts[1]),
                        float(parts[2])
                    )
                    equations.append(eq)
    except FileNotFoundError:
        print("File not found")
        return

    no_solution = []
    one_solution = []
    two_solution = []
    inf_solution = []

    for eq in equations:
        roots = eq.solve()
        if roots == 'inf':
            inf_solution.append(eq)
        elif len(roots) == 0:
            no_solution.append(eq)
        elif len(roots) == 1:
            one_solution.append((eq, roots[0]))
        elif len(roots) == 2:
            two_solution.append(eq)


    print("---Analising---")
    print("No Solutions:")
    for eq in no_solution:
        eq.show()
    print("One Solutions:")
    for eq in one_solution:
        eq.show()
    print("Two Solutions:")
    for eq in two_solution:
        eq.show()
    print("Inf Solutions:")
    for eq in inf_solution:
        eq.show()

    if one_solution:
        min_eq = min(one_solution, key=lambda x: x[1])
        max_eq = max(one_solution, key=lambda x: x[1])

        print("smallest root:")
        min_eq[0].show()
        print("x =", min_eq[1])

        print("largest root:")
        max_eq[0].show()
        print("x =", max_eq[1])

process_equations("input01.txt")


