# Rectangle and Square Classes

This project implements object-oriented programming concepts to create a `Rectangle` class and a `Square` class. The `Square` class is a subclass of `Rectangle` and inherits its methods and attributes.

## Installation

To use these classes in your project, simply download the module file and import it:

```python
from shape_calculator import Rectangle, Square
```

## Class Documentation

### Rectangle Class

The `Rectangle` class creates rectangles with width and height attributes.

#### Initialization

```python
rect = Rectangle(width, height)
```

#### Methods

- `set_width(width)`: Sets the width of the rectangle
- `set_height(height)`: Sets the height of the rectangle
- `get_area()`: Returns the area (width * height)
- `get_perimeter()`: Returns the perimeter (2 * width + 2 * height)
- `get_diagonal()`: Returns the diagonal ((width ** 2 + height ** 2) ** 0.5)
- `get_picture()`: Returns a string representation of the shape using "*" characters. Each line of "*" represents the width, and the number of lines represents the height. Returns "Too big for picture." if width or height exceeds 50.
- `get_amount_inside(shape)`: Takes another shape (square or rectangle) as an argument and returns how many times that shape could fit inside the rectangle without rotations.

#### String Representation

When printed, a rectangle will be displayed as: `Rectangle(width=5, height=10)`

### Square Class

The `Square` class is a subclass of `Rectangle` with equal width and height.

#### Initialization

```python
sq = Square(side)
```

#### Additional Methods

- `set_side(side)`: Sets both width and height to the same value

The `Square` class inherits all methods from `Rectangle`, but the `set_width` and `set_height` methods will set both dimensions to maintain a square shape.

#### String Representation

When printed, a square will be displayed as: `Square(side=9)`

## Usage Example

```python
# Create a rectangle
rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

# Create a square
sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

# Check how many squares fit inside the rectangle
rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
```

## Expected Output

When running the usage example above, you should see the following output:

```bash
50
26
Rectangle(width=10, height=3)
**********
**********
**********

81
5.656854249492381
Square(side=4)
****
****
****
****

8
```
