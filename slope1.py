# Write a program to find the m(slope) when intercept in y-axis is -5 and passing through the point (2,3)

def find_slope(x, y, b):
    # y = mx + b  =>  m = (y - b) / x
    m = (y - b) / x
    return m

x, y = 2, 3
b = -5

slope = find_slope(x, y, b)
print("The slope (m) of the line is:", slope)
