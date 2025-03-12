# Arithmetic Arranger

This project implements a function that takes arithmetic addition and subtraction problems and arranges them vertically as taught in primary schools.

## Description

The `arithmetic_arranger` function receives a list of strings that are arithmetic problems and returns the problems arranged vertically and side-by-side. Optionally, the function can display the answers to the problems.

## Functionality

- Arranges addition and subtraction problems in vertical format
- Correctly right-aligns the numbers
- Option to show calculation results
- Error handling for incorrect inputs

## Rules

The function will return the correct conversion if the supplied problems are properly formatted. Otherwise, it will return an error message.

### Situations that will return an error

- If there are **too many problems** supplied to the function. The limit is **five**, anything more will return: `'Error: Too many problems.'`
- The appropriate operators the function will accept are **addition** and **subtraction**. Multiplication and division will return an error: `"Error: Operator must be '+' or '-'."`
- Each number (operand) should only contain digits. Otherwise, the function will return: `'Error: Numbers must only contain digits.'`
- Each operand has a max of four digits in width. Otherwise, the error string returned will be: `'Error: Numbers cannot be more than four digits.'`

### Formatting rules

- There should be a single space between the operator and the longest of the two operands
- The operator will be on the same line as the second operand
- Numbers should be right-aligned
- There should be four spaces between each problem
- There should be dashes at the bottom of each problem that run along the entire length of each problem

## Examples

### Example 1

```python
arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
```

Output:

```bash
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
```

### Example 2

```python
arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
```

Output:

```bash
  32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474
```

## Usage

```python
from arithmetic_arranger import arithmetic_arranger

# Without showing answers
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))

# Showing answers
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
```
