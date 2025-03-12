# Probability Simulator

This project implements a probability simulator for drawing balls from a hat, similar to an urn experiment without replacement. The program helps estimate the probability of drawing specific combinations of colored balls through repeated random experiments.

## Installation

To use this probability simulator in your project, simply download the `prob_calculator.py` file and import it:

```python
from prob_calculator import Hat, experiment
```

## Class and Function Documentation

### Hat Class

The `Hat` class represents a hat containing colored balls.

#### Initialization

The `Hat` class accepts a variable number of keyword arguments specifying the number of balls of each color:

```python
hat = Hat(yellow=3, blue=2, green=6)
```

Each hat is created with at least one ball. The arguments are converted to a `contents` instance variable, which is a list of strings with one item for each ball in the hat.

Example: If `hat = Hat(red=2, blue=1)`, then `contents` would be `['red', 'red', 'blue']`.

#### Methods

- `draw(number)`: Removes and returns a specified number of randomly selected balls from the hat. If the number of balls requested exceeds the available quantity, all balls are returned.

### experiment Function

The `experiment` function calculates the approximate probability of drawing a specific combination of balls.

#### Parameters

- `hat`: A Hat object containing balls (will be copied inside the function)
- `expected_balls`: A dictionary indicating the exact group of balls to attempt to draw
- `num_balls_drawn`: The number of balls to draw in each experiment
- `num_experiments`: The number of experiments to perform

#### Return Value

Returns a probability value (a number between 0 and 1) representing the likelihood of drawing the specified combination.

## Usage Example

Here's an example of how to use the Hat class and experiment function:

```python
# Create a hat with 6 black balls, 4 red balls, and 3 green balls
hat = Hat(black=6, red=4, green=3)

# Calculate the probability of drawing at least 2 red balls and 1 green ball
# when drawing 5 balls from the hat, based on 2000 experiments
probability = experiment(
    hat=hat,
    expected_balls={'red': 2, 'green': 1},
    num_balls_drawn=5,
    num_experiments=2000
)

print(probability)
```

## Expected Output

The output will be a decimal representing the probability, such as:

```bash
0.356
```

Note that since this is based on random sampling, the exact probability value will vary slightly each time the program is run. Increasing the number of experiments will generally lead to more accurate probability estimates.

## Implementation Notes

- The `experiment` function performs multiple random draw experiments and counts the successes.
- A "success" occurs when the drawn balls contain at least the quantity of each color specified in `expected_balls`.
- The probability is calculated as the number of successful experiments divided by the total number of experiments.
- The modules `random` and `copy` are used for the implementation.
