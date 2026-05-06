# Write a program to write the equation of a straight line if slope is 2/3 and x-intercept is 4.

def line_equation(m, a):
    # For x-intercept 'a':  a = -b/m  =>  b = -m * a
    b = -m * a
    return b

m = 2/3          # slope
a = 4            # x-intercept

b = line_equation(m, a)
print("Equation of line: y =", m, "x +", b)
