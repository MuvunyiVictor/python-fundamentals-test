# MATH SOLVER ASSIGNMENT
# Complete all functions below and test them with the given values

### PROBLEM 1: Basic Expression with One Variable
def calculate_expression(x):
    """
    Calculate: 3x² + 2x - 5 when x = 4
    Expected Output: 51
    """
    # YOUR CODE HERE
    pass

### PROBLEM 2: Expression with Multiple Variables  
def expression_multiple_variables(a, b, c):
    """
    Calculate: 2a + 3b - c when a=5, b=2, c=3
    Expected Output: 13
    """
    # YOUR CODE HERE
    pass

### PROBLEM 3: Grouping Like Terms
def group_like_terms(x, y):
    """
    Simplify: (3x + 2y + 5x - y) and calculate when x=2, y=3
    Expected Output: 19
    """
    # YOUR CODE HERE
    pass

### PROBLEM 4: Solve Linear Equation
def solve_linear_equation():
    """
    Solve: 2x + 5 = 13 and return x
    Expected Output: 4
    """
    # YOUR CODE HERE
    pass

### PROBLEM 5: Solve Another Linear Equation
def solve_linear_equation2():
    """
    Solve: 3(x - 4) = 15 and return x
    Expected Output: 9
    """
    # YOUR CODE HERE
    pass

### PROBLEM 6: System of Equations
def solve_system_equations():
    """
    Solve:
    2x + y = 10
    x - y = 2
    Return (x, y)
    Expected Output: (4, 2)
    """
    # YOUR CODE HERE
    pass

### PROBLEM 7: Unit Conversion - Length
def convert_meters_to_feet(meters):
    """
    Convert 25 meters to feet (1 meter = 3.28084 feet)
    Expected Output: 82.021
    """
    # YOUR CODE HERE
    pass

### PROBLEM 8: Unit Conversion - Temperature  
def convert_celsius_to_fahrenheit(celsius):
    """
    Convert 100° Celsius to Fahrenheit (F = C × 9/5 + 32)
    Expected Output: 212
    """
    # YOUR CODE HERE
    pass

### PROBLEM 9: Check Linear Inequality
def check_inequality1(x):
    """
    Check if x=7 satisfies: 3x + 2 > 20
    Return True or False
    Expected Output: True
    """
    # YOUR CODE HERE
    pass

### PROBLEM 10: Another Inequality Check
def check_inequality2(x):
    """
    Check if x=3 satisfies: 2x - 5 ≤ 1  
    Return True or False
    Expected Output: True
    """
    # YOUR CODE HERE
    pass

### PROBLEM 11: Expression with Fractions
def expression_with_fractions(x, y):
    """
    Calculate: (1/2)x + (2/3)y when x=6, y=9
    Expected Output: 9
    """
    # YOUR CODE HERE
    pass

### PROBLEM 12: Perimeter Calculator
def calculate_perimeter(length, width):
    """
    Calculate perimeter of rectangle with length=8 and width=5
    Expected Output: 26
    """
    # YOUR CODE HERE
    pass

### PROBLEM 13: Area of Triangle
def calculate_triangle_area(base, height):
    """
    Calculate area of triangle with base=10 and height=4
    Expected Output: 20
    """
    # YOUR CODE HERE
    pass

### PROBLEM 14: Distance Formula
def calculate_distance(x1, y1, x2, y2):
    """
    Calculate distance between points (2,3) and (5,7)
    Formula: √[(x₂-x₁)² + (y₂-y₁)²]
    Expected Output: 5.0
    """
    # YOUR CODE HERE
    pass

### PROBLEM 15: Simple Interest Calculator
def calculate_simple_interest(principal, rate, time):
    """
    Calculate simple interest: Principal=1000, Rate=5%, Time=2 years
    Expected Output: 100
    """
    # YOUR CODE HERE
    pass

# CONCEPTUAL QUESTIONS - WRITE YOUR ANSWERS AS COMMENTS BELOW

"""
QUESTION 16: Data Types as Classes

When we write:
x = 5 - this creates an instance of the ______ class
name = "hello" - this creates an instance of the ______ class  
price = 19.99 - this creates an instance of the ______ class

Explain in your own words what this means:

YOUR ANSWER HERE

"""

"""
QUESTION 17: Nested Loops and CSV Representation

A nested loop is when...

Can a list of lists represent CSV data? 

Explanation:

In a list of lists like [[1,2,3], [4,5,6], [7,8,9]]:
- Each inner list represents...
- Each item in the inner list represents...
- This is similar to a CSV file because...

YOUR ANSWER HERE

"""

# TEST YOUR FUNCTIONS HERE
if __name__ == "__main__":
    # Test each function with the given values
    print("Testing Problem 1:", calculate_expression(4))
    print("Testing Problem 2:", expression_multiple_variables(5, 2, 3))
    print("Testing Problem 3:", group_like_terms(2, 3))
    print("Testing Problem 4:", solve_linear_equation())
    print("Testing Problem 5:", solve_linear_equation2())
    print("Testing Problem 6:", solve_system_equations())
    print("Testing Problem 7:", convert_meters_to_feet(25))
    print("Testing Problem 8:", convert_celsius_to_fahrenheit(100))
    print("Testing Problem 9:", check_inequality1(7))
    print("Testing Problem 10:", check_inequality2(3))
    print("Testing Problem 11:", expression_with_fractions(6, 9))
    print("Testing Problem 12:", calculate_perimeter(8, 5))
    print("Testing Problem 13:", calculate_triangle_area(10, 4))
    print("Testing Problem 14:", calculate_distance(2, 3, 5, 7))
    print("Testing Problem 15:", calculate_simple_interest(1000, 5, 2))
