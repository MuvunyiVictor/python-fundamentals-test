# Python Fundamentals & Computational Thinking Assessment

## Instructions
1. Complete all 15 programming problems in the `math_solver.py` file
2. Each function has SPECIFIC input values to test with - call your functions with these values
3. Test that your solutions work by running the code and checking the output
4. Answer the thre conceptual questions at the end in the comments
5. Submit by pushing your completed code

---

## Programming Problems

### Problem 1: Basic Expression with One Variable
Write a function that calculates: 3x² + 2x - 5 when x = 4

### Problem 2: Expression with Multiple Variables
Write a function that calculates: 2a + 3b - c when a=5, b=2, c=3

### Problem 3: Grouping Like Terms
Write a function that simplifies: (3x + 2y + 5x - y) and calculates the result when x=2, y=3

### Problem 4: Solve Linear Equation
Write a function that solves: 2x + 5 = 13 and returns the value of x

### Problem 5: Solve Another Linear Equation
Write a function that solves: 3(x - 4) = 15 and returns the value of x

### Problem 6: System of Equations
Write a function that solves:
2x + y = 10
x - y = 2
Return the values of x and y as a tuple (x, y)

### Problem 7: Unit Conversion - Length
Write a function that converts 25 meters to feet (1 meter = 3.28084 feet)

### Problem 8: Unit Conversion - Temperature
Write a function that converts 100° Celsius to Fahrenheit (F = C × 9/5 + 32)

### Problem 9: Check Linear Inequality
Write a function that checks if x=7 satisfies: 3x + 2 > 20

### Problem 10: Another Inequality Check
Write a function that checks if x=3 satisfies: 2x - 5 ≤ 1

### Problem 11: Expression with Fractions
Write a function that calculates: (1/2)x + (2/3)y when x=6, y=9

### Problem 12: Perimeter Calculator
Write a function that calculates the perimeter of a rectangle with length=8 and width=5

### Problem 13: Area of Triangle
Write a function that calculates the area of a triangle with base=10 and height=4

### Problem 14: Distance Formula
Write a function that calculates the distance between points (2,3) and (5,7) using: √[(x₂-x₁)² + (y₂-y₁)²]

### Problem 15: Simple Interest Calculator
Write a function that calculates simple interest: Principal=1000, Rate=5%, Time=2 years

---

## Conceptual Questions

### Question 16: Data Types as Classes
In Python, even basic data types like integers, floats, and strings are actually objects created from classes. When you write `x = 5`, you're creating an instance of which class? What about `name = "hello"` and `price = 19.99`?

### Question 17: Nested Loops and Data Structures
**Research Task:** A nested loop is when you have one loop inside another loop. For example:
```python
for i in range(3):
    for j in range(2):
        print(i, j)
Now research: Can a list of lists (like [[1,2,3], [4,5,6], [7,8,9]]) be used to represent data similar to a CSV file? Explain how this might work and what each part represents.


### Problem 6: CPU Execution Process
Complete the following paragraph by selecting the appropriate words from this list:
[**fetch, decode, execute, memory, instructions, control, flags, address, jump, registers**]

"The Central Processing Unit (CPU) follows a continuous cycle to process programs. First, it ______ instructions from ______. Then it ______ each instruction to understand what operation to perform. Finally, it ______ the instruction. For flow control, the CPU uses ______ that determine whether to perform a ______ to a different ______. Status ______ help the CPU make these decisions by storing the results of previous operations. Temporary data is stored in ______ during processing."
### Testing Your Code
For each function, call it with the given values and print the result.
Example:
# Test Problem 1
result1 = calculate_expression(4)
print(f"Problem 1 result: {result1}")

Good luck! Show me how you can use Python to solve real mathematical problems!
