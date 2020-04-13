# Strings

## Besides numbers, Python can also manipulate strings, which can be expressed in several ways. They can be enclosed in single quotes ('...') or double quotes ("...") with the same result 2. \ can be used to escape quotes:

```python
>>> 'spam eggs'  # single quotes
'spam eggs'
>>> 'doesn\'t'  # use \' to escape the single quote...
"doesn't"
>>> "doesn't"  # ...or use double quotes instead
"doesn't"
>>> '"Yes," they said.'
'"Yes," they said.'
>>> "\"Yes,\" they said."
'"Yes," they said.'
>>> '"Isn\'t," they said.'
'"Isn\'t," they said.'
```

## If you don’t want characters prefaced by \ to be interpreted as special characters, you can use raw strings by adding an r before the first quote:

```python
>>> print('C:\some\name')  # here \n means newline!
C:\some
ame
>>> print(r'C:\some\name')  # note the r before the quote
C:\some\name
```

## String literals can span multiple lines. One way is using triple-quotes: """...""" or '''...'''. End of lines are automatically included in the string, but it’s possible to prevent this by adding a \ at the end of the line. The following example:

```python
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")
```

## Strings can be concatenated (glued together) with the + operator,and repeated with *:

```python
# 3 times 'un', followed by 'ium'
3 * 'un' + 'ium'
```

## Strings can be indexed, with the first character having index 0. There is no separate character type; a character is simply a string of size one:

```python
word = 'Python'
word[0]  # character in position 0
'P'
word[5]  # character in position 5
'n'
```
## In addition to indexing, slicing is also supported. While indexing is used to obtain individual characters, slicing allows you to obtain substring:

```python
word = 'Python'
>>> word[0:2]  # characters from position 0 (included) to 2 (excluded)
'Py'
>>> word[2:5]  # characters from position 2 (included) to 5 (excluded)
'tho'
```

## Python strings cannot be changed — they are immutable. Therefore, assigning to an indexed position in the string results in an error:
```python
word[0] = 'J'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
```

## If you need a different string, you should create a new one:
```python
'J' + word[1:]
'Jython'
```

## The built-in function len() returns the length of a string:
```python
s = 'supercalifragilisticexpialidocious'
len(s)
34
```
