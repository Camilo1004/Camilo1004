# Budget App

This project implements a budget application that helps track expenses across different categories.

## Description

The Budget App provides functionality to manage budgets by category. It allows users to:

- Create budget categories
- Make deposits and withdrawals
- Transfer funds between categories
- Generate a visual chart showing spending percentages by category

## Components

### Category Class

The `Category` class enables the creation of budget categories and provides methods to manage funds:

#### Methods

- `deposit(amount, description)`: Adds funds to the category
- `withdraw(amount, description)`: Removes funds from the category
- `get_balance()`: Returns the current balance
- `transfer(amount, destination)`: Transfers funds to another category
- `check_funds(amount)`: Verifies if sufficient funds are available

#### Output Format

When a `Category` object is printed, it displays:

- A title with the category name centered between asterisks
- A list of transactions showing descriptions and amounts
- The total balance

### Spend Chart Function

The `create_spend_chart` function generates a bar chart showing the percentage spent in each category.

#### Features

- Shows spending percentages from 0-100%
- Bar heights are based on withdrawal amounts only
- Category names are displayed vertically below the bars
- Percentages are rounded down to the nearest 10

## Installation

Save the budget.py file in your project directory:

```python
# budget.py
class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
    
    # Implementation of methods...
    
def create_spend_chart(categories):
    # Implementation of chart function...
```

## Usage Examples

### Example 1: Basic Usage

```python
# main.py
from budget import Category, create_spend_chart

# Create a budget category
food = Category("Food")

# Make deposits and withdrawals
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")

# Create another category
clothing = Category("Clothing")

# Transfer between categories
food.transfer(50, clothing)

# Print a category
print(food)
```

Output:

```bash
*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant and more foo -15.89
Transfer to Clothing    -50.00
Total: 923.96
```

### Example 2: Creating a Spend Chart

```python
# main.py
from budget import Category, create_spend_chart

# Create categories
food = Category("Food")
entertainment = Category("Entertainment")
business = Category("Business")

# Add funds to each category
food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")

# Make withdrawals
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)

# Generate the spend chart
categories = [food, entertainment, business]
print(create_spend_chart(categories))
```

Output:

```bash
Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60| o        
 50| o        
 40| o        
 30| o        
 20| o  o     
 10| o  o  o  
  0| o  o  o  
    ----------
     F  E  B  
     o  n  u  
     o  t  s  
     d  e  i  
        r  n  
        t  e  
        a  s  
        i  s  
        n     
        m     
        e     
        n     
        t     
```

### Example 3: Full Usage Example

```python
# main.py
from budget import Category, create_spend_chart

def main():
    # Create budget categories
    rent = Category("Rent")
    groceries = Category("Groceries")
    entertainment = Category("Entertainment")
    savings = Category("Savings")

    # Add initial deposits
    rent.deposit(1200, "monthly rent money")
    groceries.deposit(500, "monthly grocery budget")
    entertainment.deposit(300, "entertainment funds")
    savings.deposit(2000, "initial savings")

    # Make withdrawals
    rent.withdraw(1200, "paying rent")
    groceries.withdraw(120.57, "weekly shopping")
    groceries.withdraw(85.23, "second week shopping")
    entertainment.withdraw(50, "movie night")
    entertainment.withdraw(25.55, "streaming services")

    # Transfer some money from savings to groceries
    savings.transfer(100, groceries)

    # Check balances
    print(f"Rent balance: ${rent.get_balance()}")
    print(f"Groceries balance: ${groceries.get_balance()}")
    print(f"Entertainment balance: ${entertainment.get_balance()}")
    print(f"Savings balance: ${savings.get_balance()}")

    # Print detailed information for each category
    print("\nDetailed category information:")
    print(rent)
    print()
    print(groceries)
    print()
    print(entertainment)
    print()
    print(savings)

    # Create a spending chart
    categories = [rent, groceries, entertainment, savings]
    print("\nSpending Chart:")
    print(create_spend_chart(categories))

if __name__ == "__main__":
    main()
```

Example Output:

```bash
Rent balance: $0.0
Groceries balance: $394.2
Entertainment balance: $224.45
Savings balance: $1900.0

Detailed category information:
*************Rent*************
monthly rent money      1200.00
paying rent            -1200.00
Total: 0.00

************Groceries************
monthly grocery budget   500.00
weekly shopping         -120.57
second week shopping     -85.23
Transfer from Savings    100.00
Total: 394.20

**********Entertainment**********
entertainment funds      300.00
movie night              -50.00
streaming services       -25.55
Total: 224.45

************Savings************
initial savings         2000.00
Transfer to Groceries   -100.00
Total: 1900.00

Spending Chart:
Percentage spent by category
100|          
 90|          
 80| o        
 70|          
 60|          
 50|          
 40|          
 30|    o     
 20|    o  o  
 10|    o  o  
  0| o  o  o  
    ----------
     R  G  E  S
     e  r  n  a
     n  o  t  v
     t  c  e  i
        e  r  n
        r  t  g
        i  a  s
        e  i   
        s  n   
           m   
           e   
           n   
           t   
```

## Implementation Notes

- The `Category` class maintains a ledger as a list of dictionaries
- Each transaction is stored with an amount and description
- Withdrawals are stored as negative amounts
- The spend chart calculates percentages based only on withdrawals
