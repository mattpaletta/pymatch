import re
from re import Pattern

class etc(object):
    pass

class Regex(object):
    __slots__ = ["_value", "_re"]

    def __init__(self, value: str):
        self._re = re.compile(value)
        self._value = value

    def value(self) -> str:
        return self._value

    def re(self) -> Pattern:
        return self._re

    def matches(self, value) -> bool:
        return bool(self._re.match(value))

def match(patterns, value):
    p = _compile(patterns)
    return p(value)

def pattern(*args):
    return _compile(args)

def _compile(patterns):
    def find_function(value):
        for p, func in patterns:
            if isinstance(p, Regex) and p.matches(value):
                return func
            if type(p) is type and type(value) is p:
                return func
            if (type(p) is list and type(value) is list) or \
                    (type(p) is tuple and type(value) is tuple):
                # if all items match
                all_items_match = True
                for i in range(max(len(p), len(value))):
                    if not all_items_match:
                        break
                    # as long as they both have values
                    if i < len(p) and i < len(value):
                        p_value = p[i]
                        v_value = value[i]
                        if p_value != v_value and not (type(p_value) is type and type(v_value) is p_value) and not p_value is etc:
                            all_items_match = False
                    elif i < len(p) and len(p) > 0 and not isinstance(p[-1], etc):
                        # We still have more in the pattern, not a match
                        # unless the last item is etc.
                        all_items_match = False
                    else:
                        # If the value continues, it's true
                        all_items_match = True
                        break
                if all_items_match:
                    return func

            # Check to see if their types match
            for t in [int, str, float, bool]:
                if type(p) is t and type(value) is t \
                    and p == value:
                        return func
        return None

    def matches(value):
        func = find_function(value)
        if func is not None:
            if type(value) is tuple:
                return func(*value)
            else:
                return func(value)

    return matches
