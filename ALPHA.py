
import math

# Circle
def circle_area(radius):
    return math.pi * radius ** 2

def circle_circumference(radius):
    return 2 * math.pi * radius

# Square
def square_area(side_length):
    return side_length ** 2

def square_perimeter(side_length):
    return 4 * side_length

# Rectangle
def rectangle_area(length, width):
    return length * width

def rectangle_perimeter(length, width):
    return 2 * (length + width)

# Triangle
def triangle_area(base, height):
    return 0.5 * base * height

def triangle_perimeter(a, b, c):
    return a + b + c

# Example Usage
radius = 5
side_length = 4
length = 6
width = 3
base = 5
height = 8
a, b, c = 3, 4, 5  # Sides of a triangle

# Circle calculations
print("Circle area:", circle_area(radius))
print("Circle circumference:", circle_circumference(radius))

# Square calculations
print("Square area:", square_area(side_length))
print("Square perimeter:", square_perimeter(side_length))

# Rectangle calculations
print("Rectangle area:", rectangle_area(length, width))
print("Rectangle perimeter:", rectangle_perimeter(length, width))

# Triangle calculations
print("Triangle area:", triangle_area(base, height))
print("Triangle perimeter:", triangle_perimeter(a, b, c))
Explanation:
Circle:
circle_area(radius) calculates the area using 
𝜋
𝑟
2
πr 
2
 .
circle_circumference(radius) calculates the circumference using 
2
𝜋
𝑟
2πr.
Square:
square_area(side_length) calculates the area using 
side
2
side 
2
 .
square_perimeter(side_length) calculates the perimeter using 
4
×
side
4×side.
Rectangle:
rectangle_area(length, width) calculates the area using 
length
×
width
length×width.
rectangle_perimeter(length, width) calculates the perimeter using 
2
×
(
length
+
width
)
2×(length+width).
Triangle:
triangle_area(base, height) calculates the area using 
1
2
×
base
×
height
2
1
​
 ×base×height.
triangle_perimeter(a, b, c) calculates the perimeter by adding all three sides.
