# Numbers

```python
>>> 2 + 2
4
>>> 50 - 5*6
20
>>> (50 - 5*6) / 4
5.0
>>> 8 / 5  # division always returns a floating point number
1.6
```
## The integer numbers (e.g. 2, 4, 20) have type *int*, the ones with a fractional part (e.g. 5.0, 1.6) have type *float*.

## Division (/) always returns a float. To do *floor division* and get an integer result (discarding any fractional result) you can use the // operator; to calculate the remainder you can use %:

```python
>>> 17 / 3  # classic division returns a float
5.666666666666667
>>>
>>> 17 // 3  # floor division discards the fractional part
5
>>> 17 % 3  # the % operator returns the remainder of the division
2
>>> 5 * 3 + 2  # result * divisor + remainder
17
```

## With Python, it is possible to use the ** operator to calculate powers

```python
>>> 5 ** 2  # 5 squared
25
>>> 2 ** 7  # 2 to the power of 7
128
```

## The equal sign (=) is used to assign a value to a variable.

```python
>>> width = 20
>>> height = 5 * 9
```
