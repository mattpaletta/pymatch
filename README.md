# pymatch
Python Pattern Matching
[![Build Status](https://travis-ci.com/mattpaletta/pymatch.svg?token=ysncAybhRTtbpjrpSW8S&branch=master)](https://travis-ci.com/mattpaletta/pymatch)

## Instalation
PyMatch has no external dependencies.
To install pymatch:
```bash
pip install git+://github.com/mattpaletta/pymatch.git
```

## Getting Started
You can see examples in `tests/`

There are two main functions.  They allow for slightly different coding patterns.  Here is a basic example written both ways.
```python
from pymatch import match, pattern

# written with match
r1 = match([
	(str, lambda s: s),
	(int, lambda i: i + 1)
], "hello world")

# written with pattern
m = pattern(
	(str, lambda s: s),
	(int, lambda i: i + 1)
)
r2 = m("hello world")
assert r1 == r2
```

`pattern` allows you to write the pattern once, and save it.  The performance is the same for both functions.  If multiple patterns match, the first one will be used.

## Matching
### Basic Values
```python
from pymatch import match
assert match([
	(3, lambda a: 4),
	(int, lambda i: i - 1)
], 3) == 4
```

### Basic Types
```python
from pymatch import match
assert match([
	(int, lambda i: i + 1),
	(float, lambda f: f + 0.5),
	(str, lambda s: "goodbye"),
	(bool, lambda b: not b)
], 3) == 4
```

### Tuples (values, types, etc.)
```python
from pymatch import pattern, etc
m = pattern(
	((1, 2, 3), lambda i, j, k: 9),
	((int, int, 3), lambda: i, j, k: i + j - k),
	((1, 2, etc), lambda: i, j, k, l: i + j + k + l)
	((int, int, int), lambda i, j, k: i + j + k),
)

assert m( (1, 2, 3) ) == 9
assert m( (4, 5, 3) ) == 6
assert m( (1, 2, 4, 5) ) == 12
assert m( (4, 5, 6) ) == 15
```
### Regex
```python
from pymatch import match, Regex
assert match([
	(Regex("^abc[a-z]8"), lambda s: "goodbye")
], "abcdefg") == "goodbye"
```

## Information

### Questions, Comments, Concerns, Queries, Qwibbles?

If you have any questions, comments, or concerns please leave them in the GitHub
Issues tracker:

https://github.com/mattpaletta/pymatch/issues

### Bug reports

If you discover any bugs, feel free to create an issue on GitHub. Please add as much information as possible to help us fixing the possible bug. We also encourage you to help even more by forking and sending us a pull request.

https://github.com/mattpaletta/pymatch/issues

## Maintainers

* Matthew Paletta (https://github.com/mattpaletta)

## License

GPL-3.0 License. Copyright 2020 Matthew Paletta. http://mrated.ca
