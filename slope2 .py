# Write a program to find the value of slope when it is passing through origin and point (3,5)

def find_slope(x1, y1, x2, y2):
    # Slope m = (y2 - y1) / (x2 - x1)
    m = (y2 - y1) / (x2 - x1)
    return m

x1, y1 = 0, 0       # Origin
x2, y2 = 3, 5       # Second point

slope = find_slope(x1, y1, x2, y2)
print("The slope of the line is:", slope)
