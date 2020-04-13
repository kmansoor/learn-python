# Control Flow Tools

## `if` Statement
```python
x = int(input("Please enter an integer: "))
Please enter an integer: 42
if x < 0:
    x = 0
    print('Negative changed to zero')
 elif x == 0:
    print('Zero')
 elif x == 1:
    print('Single')
 else:
    print('More')
```

## `for` Statement
```python
num = [1, 2, 3, 4, 5]
for a in num:
    print(a)

name = 'John Dingle'
for c in name:
    print(c)

words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

```

## The `range()` function
### If you do need to iterate over a sequence of numbers, the built-in function range() comes in handy. It generates arithmetic progressions:
```python
for i in range(10):
    print(i)
```
### The given end point is never part of the generated sequence; range(10) generates 10 values, the legal indices for items of a sequence of length 10. It is possible to let the range start at another number, or to specify a different increment (even negative; sometimes this is called the ‘step’):
```python
for x in range(5, 10):
    print(x)


for x in range(0, 10, 3):
   print(x)


for x in range(-10, -100, -30):
    print(x)
```

### To iterate over the indices of a sequence, you can combine `range()` and `len()` as follows:
```python
a = ['This', 'is', 'a', 'test']
for i in range(len(a)):
    print(i, a[i])
```

## `break` and `continue`
