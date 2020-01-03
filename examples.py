from pymatch import match, pattern, Regex, etc

def handle_tuple(i0, i1, i2):
    return i0 + i1 + i2

result = match(
    [
        (str, lambda s: print(s)),
        (Regex("^abc"), lambda s: print(s)),
        (int, lambda i: print (i + 1)),
        ((1, 2, 3), handle_tuple),
        ((int, int, 3), handle_tuple),
    ],
    "hello world")
assert result is None

m = pattern(
    (str, lambda s: print(s)),
    (int, lambda i: print (i + 1)),
    ((1, 2, 3), handle_tuple),
    ((int, int, 3), handle_tuple))

assert m("hello world") is None
assert m(0) is None
assert m((1, 2, 3)) == 6
assert m((5, 4, 3)) == 12
