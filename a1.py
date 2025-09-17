# Assignment 1: AI-Generated Python Problems
# Name: [Your Name Here]

"""
AI-Generated Problem Set

INSTRUCTIONS:
1. Document your original AI prompt below
2. Copy the problems your AI assistant generated
3. Implement solutions for each problem
4. Include comments explaining your approach
5. Test your solutions with different inputs

Remember: The goal is to LEARN, not just get working code!
"""

# =============================================================================
# PART 1: DOCUMENT YOUR AI COLLABORATION
# =============================================================================

"""
MY ORIGINAL AI PROMPT:
Hey I am high school student learning the basics of Python, could you give me 5 practice problems that involve, Variables, Conditionals, Loops, List, and Functions.

Problem 1: Temperature Converter

Topic: Variables and basic data types

Instructions:
Write a program that converts a temperature from Celsius to Fahrenheit.
Use the formula:
Fahrenheit = (Celsius × 9/5) + 32

Input: A number representing degrees in Celsius.
Output: The equivalent temperature in Fahrenheit.

Example:

Input: 25
Output: 77.0

✅ Problem 2: Even or Odd Checker

Topic: Conditionals

Instructions:
Write a program that checks whether a number is even or odd.

Input: An integer.
Output: "Even" if the number is even, otherwise "Odd".

Example:

Input: 7
Output: Odd

✅ Problem 3: Find the Maximum

Topic: Lists and loops

Instructions:
Write a function called find_max(numbers) that takes a list of numbers and returns the largest number.

Input: A list of integers.
Output: The largest integer in the list.

Example:

Input: [4, 9, 1, 22, 5]
Output: 22

✅ Problem 4: Sum of Multiples

Topic: Loops + Conditionals + Functions

Instructions:
Write a function sum_of_multiples(n) that returns the sum of all numbers from 1 to n that are divisible by 3 or 5.

Input: A positive integer n.
Output: The sum of all numbers ≤ n divisible by 3 or 5.

Example:

Input: 10
Output: 33
# (3 + 5 + 6 + 9 + 10)

✅ Problem 5: Remove Even Numbers

Topic: Lists + Loops + Functions

Instructions:
Write a function remove_evens(numbers) that takes a list of integers and returns a new list with all even numbers removed.

Input: A list of integers.
Output: A new list containing only the odd numbers.

Example:

Input: [1, 2, 3, 4, 5, 6]
Output: [1, 3, 5]
"""

# =============================================================================
# PART 2: AI-GENERATED PROBLEMS & SOLUTIONS
# =============================================================================

"""
PROBLEM 1: Temperature Converter

Topic: Variables and basic data types

Instructions:
Write a program that converts a temperature from Celsius to Fahrenheit.
"""
def cal_fahr(n):
    Celsius = 0
    n = (Celsius * 9/5) + 32
    return(n)

"""
PROBLEM 2: Even or Odd Checker

Topic: Conditionals

Instructions:
Write a program that checks whether a number is even or odd.
"""
def check(lst: int):
    even = []
    odd = []
    for num in lst:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    return even and odd

"""
PROBLEM 3: Find the Maximum

Topic: Lists and loops

Instructions:
Write a function called find_max(numbers) that takes a list of numbers and returns the largest number.

Input: A list of integers.
Output: The largest integer in the list.
"""
def find_max(lst: int):
    max_numb = lst[0]
    for num in lst[1:]:
        if num > max_numb:
            max_numb = num
    return max_numb



"""
PROBLEM 4:Sum of Multiples

Topic: Loops + Conditionals + Functions

Instructions:
Write a function sum_of_multiples(n) that returns the sum of all numbers from 1 to n that are divisible by 3 or 5.
"""
def sum_of_multiples(lst: int):
    total = 0
    for num in lst:
        if num in lst // 3 or 5:
            total += num
            return total
"""
PROBLEM 5:Remove Even Numbers

Topic: Lists + Loops + Functions

Instructions:
Write a function remove_evens(numbers) that takes a list of integers and returns a new list with all even numbers removed.
"""
def remove_even(lst: int):
    odds = []
    for num in lst:
        if num % 2 != 0:
            odds.append(num)
    return odds










# =============================================================================
# PART 3: TESTING YOUR SOLUTIONS
# =============================================================================


"""
Test all your solutions with different inputs

Add asserts if you feel comfortable


Example:
print("Testing Problem 1:")
print(f"is_even(4): {is_even(4)}")  # Should print True
print(f"is_even(7): {is_even(7)}")  # Should print False
"""
assert cal_fahr(22) == 71.6, "Calculator failed"
assert check([1, 2, 3, 4, 5]) == [2, 4] and [1, 3, 5], "Check failed"
assert find_max([1, 2, 3, 4, 5]) == 5, "Find max failed"
assert sum_of_multiples([1, 2, 3, 4, 5]) == 8, "Sum of multiples failed"
assert remove_even([1, 2, 3, 4, 5]) == [1, 3, 5], "Remove even failed"
print("Testing Problem 1:")
# Add your tests here

print("\nTesting Problem 2:")
# Add your tests here

print("\nTesting Problem 3:")
# Add your tests here

print("\nTesting Problem 4:")
# Add your tests here

print("\nTesting Problem 5:")
# Add your tests here


