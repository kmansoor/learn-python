# Defining Functions
```python
def some_func():
    print("Hello from a fine function")

#######################################
def say_hello(n):
    for i in range(1, n + 1):
        print(i, "Hello")

#######################################
def squared(a):
    result = a * a
    return result

#######################################
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end = ' ')
        a, b = b, a + b

#######################################
def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result

#######################################
#hello(10)
some_func()
say_hello(3)
print(squared(4))
```