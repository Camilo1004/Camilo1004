# Time Calculator

This project implements a function that calculates a new time by adding a duration to a start time.

## Description

The `add_time` function adds a duration to a given start time and returns the result, including information about how many days have passed and the day of the week if provided.

## Function Parameters

The function takes in:

* A start time in the 12-hour clock format (ending in AM or PM)
* A duration time that indicates the number of hours and minutes
* (Optional) A starting day of the week, case insensitive

## Functionality

The function performs the following operations:

* Adds the duration time to the start time
* Handles the conversion between AM/PM
* Tracks the number of days that pass
* Includes the day of the week in the result if a starting day was provided

## Return Format

The function returns a string with the new time and, when applicable:

* The day of the week
* If the result is the next day, it shows `(next day)` after the time
* If the result is more than one day later, it shows `(n days later)` after the time, where "n" is the number of days later

## Examples

```python
add_time('3:00 PM', '3:10')
# Returns: 6:10 PM

add_time('11:30 AM', '2:32', 'Monday')
# Returns: 2:02 PM, Monday

add_time('11:43 AM', '00:20')
# Returns: 12:03 PM

add_time('10:10 PM', '3:30')
# Returns: 1:40 AM (next day)

add_time('11:43 PM', '24:20', 'tueSday')
# Returns: 12:03 AM, Thursday (2 days later)

add_time('6:30 PM', '205:12')
# Returns: 7:42 AM (9 days later)
```

## Implementation Notes

* No Python libraries are imported to solve this challenge
* The start times are assumed to be valid times
* The minutes in the duration time will be a whole number less than 60, but the hour can be any whole number

## Usage

```python
from time_calculator import add_time

print(add_time('3:00 PM', '3:10'))
print(add_time('11:30 AM', '2:32', 'Monday'))
```
